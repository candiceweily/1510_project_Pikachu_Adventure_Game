import random
import itertools
from game_files import ROWS, COLUMNS, LEVEL_UP_EXPERIENCE, MAX_HP_BY_LEVEL, FOE_NAMES, WIN_CHANCE_BY_LEVEL
from game_files import HP_CHANGE_BY_LEVEL, XP_CHANGE_BY_LEVEL, ABILITY_BY_LEVEL
from game_files import BOSS_BATTLE_XP_NEED, BOSS_BATTLE_HP_REDUCE, BOSS_BATTLE_HIT_CHANCE


def menu() -> str:
    """
    Display the main menu for the game and prompt the user to make a choice.

    :postcondition: prompt the user to choose the desired option return the choice from the user
    :return: the choice from the user as a string
    """
    while True:
        print("\n--- Pikachu Adventure Game Menu ---")
        print("1. Start Game")
        print("2. Help")
        print("3. Exit")
        choice = input("Enter your choice (1, 2 or 3): ").strip()
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def display_help() -> None:
    """
    Display the help section for the game.

    :postcondition: print the help section for the game
    """
    print("\n--- Help & Information ---")
    print("Welcome to Pikachu Adventure Game!")
    print("Navigate Pikachu through various locations, battle foes, and level up.")
    print("Make strategic decisions to ensure Pikachu's victory.")


def make_board(rows: int, columns: int) -> dict[tuple[int, int]: str]:
    """
    Create a game board with random room descriptions.

    This function generates a board for the game with the specified number of rows and columns. Each cell on the board
    is assigned a random description from a predefined list.

    :param rows: a positive integer
    :param columns: a positive integer
    :precondition: rows and columns must be positive integer
    :postcondition: correctly create the game board which each key is a tuple and each value is a string description of
    the room
    :return: the game board as a dictionary
    """
    descriptions = ['Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Hisui']
    return {(row, col): random.choice(descriptions) for row in range(rows) for col in range(columns)}


def make_character() -> dict[str: str | int]:
    """
    Create a game character for the game.

    :precondition: character must be a dictionary
    :postcondition: correctly create the character for the game
    :return: the character as a dictionary

    >>> player_character = make_character()
    >>> player_character == {
    ... 'Name': 'Pikachu', 'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1,
    ... 'Current HP': 20, 'Max HP': 20, 'XP': 0, 'Ability': 'Thunder Shock',
    ... 'Potions': 5}
    True
    """
    return {
        "Name": "Pikachu",
        "X-coordinate": 0,
        "Y-coordinate": 0,
        "Level": 1,
        "Current HP": 20,
        "Max HP": 20,
        "XP": 0,
        "Ability": "Thunder Shock",
        "Potions": 5
    }


def display_welcome_message() -> None:
    """
    Print a welcome message and an ASCII art representation of Pikachu.
    """
    print("Welcome to Pikachu adventure game!")
    print("\033[93m" + r"""
                  \:.             .:/
                   \``._________.''/ 
                    \             / 
             .--.--, / .':.   .':. \
            /__:  /  | '::' . '::' |
               / /   |`.   ._.   .'|
              / /    |.'         '.|
             /___-_-,|.\  \   /  /.|
                  `==|:=         =:|
                     `.          .'
                       :-._____-.:
                      `''       `'' 
    """ + "\033[0m")


def describe_current_location(board: dict[tuple[int, int]: str], character: dict[str: str | int]) -> None:
    """
    Describe the current location of the character.

    :param board: board is a non-empty dictionary
    :param character: character is a non-empty dictionary
    :precondition: board is a non-empty dictionary which each key is a tuple and each value is a string description of
    the room
    :precondition: character is a non-empty dictionary that contains location and attributes
    :postcondition: correctly describe the current location of the character

    >>> player_board = {(0, 0): 'Kanto', (0, 1): 'Johto', (1, 0): 'Hisui', (1, 1): 'Sinnoh'}
    >>> player_character = {
    ... 'Name': 'Pikachu', 'X-coordinate': 0, 'Y-coordinate': 0,
    ... 'Level': 1, 'Current HP': 20, 'Max HP': 20, 'XP': 0,
    ... 'Ability': 'Thunder Shock', 'Potions': 5
    ... }
    >>> describe_current_location(player_board, player_character)
    You are in Kanto, at location (0, 0).
    >>> player_board = {(0, 0): 'Kanto', (0, 1): 'Johto', (1, 0): 'Hisui', (1, 1): 'Sinnoh'}
    >>> player_character = {
    ... 'Name': 'Pikachu', 'X-coordinate': 1, 'Y-coordinate': 1,
    ... 'Level': 1, 'Current HP': 20, 'Max HP': 20, 'XP': 0,
    ... 'Ability': 'Thunder Shock', 'Potions': 5
    ... }
    >>> describe_current_location(player_board, player_character)
    You are in Sinnoh, at location (1, 1).
    """
    location = (character["X-coordinate"], character["Y-coordinate"])
    print(f'You are in {board[location]}, at location {location}.')


def display_map_with_character_position(character: dict[str: str | int]) -> None:
    """
    Display the game board map with a 10*10 grid, and indicate where the character and the boss is.

    :param character: character is a non-empty dictionary
    :precondition: character is a non-empty dictionary that contains location and attributes
    :postcondition: correctly display the current location of the character in the map
    """
    print('Game Board Map: ')
    print("+" + "----+" * 10)
    yellow_start = "\033[1m\033[33m"
    red_start = "\033[1m\033[31m"
    color_reset = "\033[0m"

    for row, column in itertools.product(range(10), repeat=2):
        if column == 0:
            print("|", end="")
        if (row, column) == (character['X-coordinate'], character['Y-coordinate']):
            print(f" {yellow_start}⚡{color_reset}  |", end="")
        elif (row, column) == (9, 9):
            print(f" {red_start}👹{color_reset} |", end="")
        else:
            print("    |", end="")

        if column == 9:
            print("\n+" + "----+" * 10)


def get_user_choice(character: dict[str: str | int]) -> str:
    """
    Prompt the user to make a choice where to move their character or to view their character's current HP or level.

    :param character: a non-empty dictionary
    :precondition: character is a non-empty dictionary that contains location and attributes
    :postcondition: get the choice of the character or display the current HP or level correctly
    :return: the choice of the character as a string
    """
    choices = ["North", "South", "East", "West", "Show Current HP", "Show Current Level"]
    print("Where would you like to go? Or type '5' to see current HP, '6' to see current level.")
    for index, value in enumerate(choices, start=1):
        print(f'{index}: {value}')
    choice = input("Choose a direction (1/2/3/4) or type 5/6: ").strip()
    while choice not in [str(index) for index in range(1, 7)]:
        print("Invalid choice, try again.")
        choice = input("Choose a direction (1/2/3/4) or type 5/6: ").strip()
    if choice == "5":
        print(f"Current HP: {character['Current HP']}/{character['Max HP']}")
    elif choice == "6":
        print(f"Current Level: {character['Level']}")
    else:
        return choice
    return get_user_choice(character)


def validate_move(character: dict[str: str | int], direction: str) -> bool:
    """
    Determine if a move in the specified direction is valid.

    This function checks if moving the character in the given direction is possible without leaving the bounds of the
    board. Return True if the move is valid, False otherwise.

    :param character: a non-empty dictionary
    :param direction: a non-empty string
    :precondition: character must be a dictionary that contains location and attributes
    :precondition: direction must be one of '1', '2', '3', '4'
    :postcondition: correctly return the boolean result of the position
    :return: return True if the move is valid, otherwise return False

    >>> validate_move({'X-coordinate': 0, 'Y-coordinate': 0}, '1')
    False
    >>> validate_move({'X-coordinate': 2, 'Y-coordinate': 2}, '2')
    True
    >>> validate_move({'X-coordinate': 4, 'Y-coordinate': 4}, '3')
    True
    """
    x_coordinate, y_coordinate = character["X-coordinate"], character["Y-coordinate"]
    if direction == "1" and x_coordinate > 0:
        return True
    elif direction == "2" and x_coordinate < ROWS - 1:
        return True
    elif direction == "3" and y_coordinate < COLUMNS - 1:
        return True
    elif direction == "4" and y_coordinate > 0:
        return True
    else:
        return False


def move_character(character: dict[str: str | int], direction: str) -> bool:
    """
    Move the character in a specified direction if possible.

    This function updates the character's position based on the given direction. It checks whether the move leads the
    character to the final boss location. If the character reaches the boss location but doesn't meet the level or XP
    requirements, it will not allow the move and prints a message. Otherwise, the character's position is updated.

    :param character: a dictionary
    :param direction: a string
    :precondition: character is a non-empty dictionary that contains location and attributes
    :precondition: direction must be one of the strings '1', '2', '3', '4'
    :postcondition: correctly move the character to the given direction
    :return: True if the character's position is successfully updated; False if the move is invalid or the character
    cannot fight the boss due to insufficient level or XP

    >>> move_character({'X-coordinate': 5, 'Y-coordinate': 5}, '1')
    True
    >>> move_character({'X-coordinate': 0, 'Y-coordinate': 0}, '4')
    True
    >>> move_character({'X-coordinate': 9, 'Y-coordinate': 9}, '2')
    True
    """
    new_x, new_y = character["X-coordinate"], character["Y-coordinate"]
    if direction == "1":
        new_x -= 1
    elif direction == "2":
        new_x += 1
    elif direction == "3":
        new_y += 1
    elif direction == "4":
        new_y -= 1
    if (new_x, new_y) == (ROWS - 1, COLUMNS - 1):
        if character["Level"] < 3 or character["XP"] < BOSS_BATTLE_XP_NEED:
            print("You've reached the final boss location, but you're not ready to fight it. Gain more XP or level up.")
            return False
    character["X-coordinate"], character["Y-coordinate"] = new_x, new_y
    return True


def decide_use_potion(character: dict[str: str | int]) -> None:
    """
    Prompt the player to decide whether to use a potion to heal the character before a fight.

    :param character: a non-empty dictionary
    :precondition: character is a non-empty dictionary that contains location and attributes
    :postcondition: update the potion data based on the user choice and print the useful information
    """
    if character["Potions"] > 0:
        print(f"Current HP: {character['Current HP']}")
        use_potion = input("Would you like to use a potion before the fight? (1-yes/2-no): ").strip()
        if use_potion == "1":
            character["Current HP"] = min(character["Current HP"] + 5, character["Max HP"])
            character["Potions"] -= 1
            print(f"Potion used. Current HP: {character['Current HP']}. Potions left: {character['Potions']}.")
        elif use_potion != "2":
            print("Invalid input. Please enter 1 or 2.")


def calculate_battle_outcome(character: dict[str: str | int], win_chance: float, xp_change: int, hp_change: int) -> bool:
    """
    Calculate and apply the outcome of a battle based on the character's chance to win.

    :param character: a non-empty dictionary
    :param win_chance: a float
    :param xp_change: a positive integer
    :param hp_change: a positive integer
    :precondition: character is a non-empty dictionary that contains location and attributes
    :precondition: win_chance is a float between 0 and 1, xp_change and hp_change are positive integers
    :postcondition: XP is increased if character wins, decreased otherwise. If HP falls to 0 or below, the game is over
    :return: True if the character wins the battle, False otherwise
    """
    if random.random() < win_chance:
        print(f"You won the battle! XP + {xp_change}")
        character["XP"] += xp_change
        return True
    else:
        print(f"You lost the battle. HP - {hp_change}")
        character["Current HP"] -= hp_change
        if character["Current HP"] <= 0:
            print("Game Over. Pikachu has fainted.")
            return False
    return True


def handle_regular_foe_encounter(character: dict[str: str | int]) -> bool:
    """
    Simulate an encounter with a regular foe and handle the battle outcome.

    :param character: a non-empty dictionary
    :precondition: character is a non-empty dictionary that contains location and attributes
    :postcondition: XP is increased if character wins, and HP is decreased if character loses
    :return: True if the character survives the encounter, False if the character is defeated and dies

    """
    foe_name = FOE_NAMES[character["Level"] - 1]
    print(f"You encountered a {foe_name}!")
    decide_use_potion(character)
    win_chance = WIN_CHANCE_BY_LEVEL[character["Level"] - 1]
    xp_change = XP_CHANGE_BY_LEVEL[character["Level"] - 1]
    hp_change = HP_CHANGE_BY_LEVEL[character["Level"] - 1]
    return calculate_battle_outcome(character, win_chance, xp_change, hp_change)


def check_for_encounters(character: dict[str: str | int]) -> bool:
    """
    Check if the character encounters a foe and handle the encounter accordingly.

    :param character: a non-empty dictionary
    :precondition: character is a non-empty dictionary that contains location and attributes
    :postcondition: the character's state may be updated based on the battle outcome if an encounter occurs and print a
    useful message otherwise
    :return: True if the character survives the encounter or if no encounter occurs, False if the character is defeated
    and dies

    """
    encounter_chance = random.randint(1, 10)
    if encounter_chance > 5:
        return handle_regular_foe_encounter(character)
    else:
        print("No foes encountered this time.")
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


def print_congratulations() -> None:
    """
    Print a congratulatory message and an ASCII art representation to celebrate defeating the final boss.
    """
    print("You've defeated the final boss!")
    print(r""" 
               ___________
              '._==_==_=_.'
              .-\:      /-.
             | (|:.     |) |
              '-|:.     |-'
                \::.    /
                 '::. .'
                   ) (
                 _.' '._
                `"""""""` 
    """)
    print("Pikachu is enjoying the triumph!")


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
