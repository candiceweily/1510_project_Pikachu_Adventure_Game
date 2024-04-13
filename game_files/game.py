import random

from game_files import ROWS, COLUMNS, LEVEL_UP_EXPERIENCE, MAX_HP_BY_LEVEL, FOE_NAMES, WIN_CHANCE_BY_LEVEL
from game_files import HP_CHANGE_BY_LEVEL, XP_CHANGE_BY_LEVEL, ABILITY_BY_LEVEL
from game_files import BOSS_BATTLE_XP_NEED, BOSS_BATTLE_HP_REDUCE, BOSS_BATTLE_HIT_CHANCE

from game_files.game_menu import menu, display_help
from game_files.game_board import make_board
from game_files.game_character import make_character, describe_current_location
from game_files.game_navigation import display_map_with_character_position, validate_move, move_character
from game_files.game_progress import get_user_choice, decide_use_potion
from game_files.game_foe import handle_regular_foe_encounter, calculate_battle_outcome
from game_files.game_art import display_welcome_message, print_congratulations
from game_files.game_mini_games import run_math_quiz, run_treasure_hunt


def check_for_encounters(character: dict[str: str | int]) -> bool:
    """
    Check if the character encounters a challenge and handle the encounter accordingly.

    :param character: a non-empty dictionary
    :precondition: character is a non-empty dictionary that contains location and attributes
    :postcondition: the character's state may be updated based on the outcome if an encounter occurs and print a
    useful message otherwise
    :return: True if the character survives the encounter or if no encounter occurs, False if the character is defeated
    and dies
    """
    encounter_chance = random.randint(1, 10)
    if encounter_chance <= 4:
        return handle_regular_foe_encounter(character)
    elif 4 < encounter_chance <= 8:
        print("Pikachu found a challenge stone inscribed with ancient numerals!")
        xp_gained = run_math_quiz()
        if xp_gained > 0:
            character['XP'] += xp_gained
            print(f"Pikachu earns {xp_gained} XP for solving the math challenge!")
    elif 8 < encounter_chance <= 10:
        run_treasure_hunt(character)
    else:
        print("It's a peaceful moment. Nothing special happens.")
    return True


def check_level_up(character: dict[str: str | int]) -> None:
    """
    Check if the character has enough XP to level up and update the character's level and ability.

    :param character: character is a non-empty dictionary
    :precondition: character is a non-empty dictionary that contains location and attributes
    :postcondition: check if Pikachu has enough XP to level up and correctly update the level and ability

    >>> test_character = {'Level': 1, 'XP': 10, 'Max HP': 20, 'Current HP': 20}
    >>> check_level_up(test_character)
    Pikachu has leveled up to Level 2! Ability upgrades to Thunder Shower.
    >>> test_character = {'Level': 2, 'XP':30, 'Max HP': 30, 'Current HP': 30}
    >>> check_level_up(test_character)
    Pikachu has leveled up to Level 3! Ability upgrades to Thunder Storm.
    """
    level = character["Level"]
    if level < 3 and character["XP"] >= LEVEL_UP_EXPERIENCE[level - 1]:
        character["Level"] += 1
        character["Max HP"] = MAX_HP_BY_LEVEL[level]
        character["Current HP"] = character["Max HP"]
        character["Ability"] = ABILITY_BY_LEVEL[level]
        print(f'Pikachu has leveled up to Level {level + 1}! Ability upgrades to {character["Ability"]}.')


def process_battle_round(character: dict[str: str | int], boss_hp: int, round_number: int) -> tuple[int, bool, int]:
    """
    Process a single round of battle between the character and the boss, updating health points accordingly.

    In each round of the battle, this function determines whether the character successfully hits the boss based on a
    predefined hit chance. If successful, the boss's HP is reduced. Regardless of the hit's success, the boss then
    attacks the character, potentially reducing the character's HP. If the character's HP falls to 0 or below, the game
    is over.

    :param character: a non-empty dictionary
    :param boss_hp: an integer
    :param round_number: a positive integer
    :precondition: character is a non-empty dictionary that contains location and attributes
    :precondition: boss_hp is an integer representing the current boss HP
    :precondition: round_number is an integer representing the current round number
    :postcondition: process the battle and update health points accordingly

    :return: a tuple containing the updated boss's HP, a boolean indicating whether the character is still alive, and
    the next round number

    """
    print(f"Round {round_number}:")
    if random.random() < BOSS_BATTLE_HIT_CHANCE:
        boss_hp -= BOSS_BATTLE_HP_REDUCE[0]
        print(f"You hit the boss! Boss's HP is now {boss_hp}.")
    else:
        print("You missed!")
    if boss_hp > 0:
        character["Current HP"] -= BOSS_BATTLE_HP_REDUCE[1]
        print(f"The boss hit you! Your HP is now {character['Current HP']}.")
        if character["Current HP"] <= 0:
            print("Game Over. Pikachu has fainted.")
            return boss_hp, False, round_number
    return boss_hp, True, round_number + 1


def final_boss_battle(character: dict[str: str | int]) -> bool:
    """
    Conduct the final boss battle of the game.

    :param character: a non-empty dictionary
    :precondition: character is a non-empty dictionary that contains location and attributes
    :postcondition: update the character's HP based on battle outcomes, end the battle when either party's HP reaches
    zero or below
    :return: True if the character defeats the boss and survives the battle, False otherwise
    """
    boss_hp = 50
    round_number = 1
    print("The final boss battle begins!")
    while boss_hp > 0 and character["Current HP"] > 0:
        boss_hp, player_alive, round_number = process_battle_round(character, boss_hp, round_number)
        if not player_alive:
            return False
    print_congratulations()
    return True


def game() -> None:
    """
    Assemble the main game loop for a grid-based adventure game.
    """
    choice = menu()

    if choice == "1":
        display_welcome_message()
        board = make_board(ROWS, COLUMNS)
        character = make_character()
        display_map_with_character_position(character)

        while True:
            describe_current_location(board, character)
            direction = get_user_choice(character)
            if validate_move(character, direction):
                if move_character(character, direction):
                    display_map_with_character_position(character)
                    if (character["X-coordinate"], character["Y-coordinate"]) == (ROWS - 1, COLUMNS - 1):
                        if character["Level"] >= 3 and character["XP"] >= BOSS_BATTLE_XP_NEED:
                            if final_boss_battle(character):
                                print("Congratulations! Pikachu completes the game!")
                                return
                            else:
                                print("Pikachu is beaten by the final boss. Game over.")
                                return
                        else:
                            print("You've reached the final boss location, but you're not ready to fight it. "
                                  "Gain more XP or level up.")
                    else:
                        if not check_for_encounters(character):
                            break
                else:
                    print("Move not possible. Choose a different direction or meet the requirements to face the boss.")
                check_level_up(character)
            else:
                print("Invalid move. Please choose a different direction.")
    elif choice == "2":
        display_help()
        return game()
    elif choice == "3":
        print("Exiting the game. Goodbye!")
        return


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
