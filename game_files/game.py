import random
from game_files import ROWS, COLUMNS, LEVEL_UP_EXPERIENCE, MAX_HP_BY_LEVEL, ABILITY_BY_LEVEL, FOE_NAMES, WIN_CHANCE_BY_LEVEL
from game_files import GUESS_GAME_NAME, GUESS_GAME_HP_CHANGE_BY_LEVEL, GUESS_GAME_XP_CHANGE_BY_LEVEL, GUESS_GAME_RANGE
from game_files import HP_CHANGE_BY_LEVEL, XP_CHANGE_BY_LEVEL, BOSS_BATTLE_XP_NEED, BOSS_BATTLE_HP_REDUCE, BOSS_BATTLE_HIT_CHANCE


def make_board(rows: int, columns: int) -> dict:
    descriptions = ['Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Hisui']
    return {(row, col): random.choice(descriptions) for row in range(rows) for col in range(columns)}


def make_character() -> dict:
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
    print("Welcome to Pikachu adventure game!")
    print(r"""
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
    """)


def describe_current_location(board: dict, character: dict) -> None:
    location = (character["X-coordinate"], character["Y-coordinate"])
    print(f'You are in {board[location]}, at location {location}.')


def display_map_with_character_position(character: dict) -> None:
    print('Game Board Map: ')
    print("+" + "----+" * 10)
    yellow_start = "\033[1m\033[33m"
    red_start = "\033[1m\033[31m"
    color_reset = "\033[0m"
    for row in range(10):
        print("|", end="")
        for column in range(10):
            if (row, column) == (character['X-coordinate'], character['Y-coordinate']):
                print(f" {yellow_start}P{color_reset}  |", end="")
            elif (row, column) == (9, 9):
                print(f" {red_start}B{color_reset}  |", end="")
            else:
                print("    |", end="")
        print("\n+" + "----+" * 10)


def get_user_choice(character: dict) -> str:
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


def validate_move(character: dict, direction: str) -> bool:
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


def move_character(character: dict, direction: str) -> bool:
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


def encounter_foe(character: dict) -> bool:
    current_x, current_y = character["X-coordinate"], character["Y-coordinate"]
    if current_x == ROWS - 1 and current_y == COLUMNS - 1:
        return True

    encounter_chance = random.randint(1, 10)
    if encounter_chance > 5:
        foe_name = FOE_NAMES[character["Level"] - 1]
        print(f"You encountered a {foe_name}!")
        if character["Potions"] > 0:
            print(f"Current HP: {character['Current HP']}")
            use_potion = input("Would you like to use a potion before the fight? (1-yes/2-no): ").strip()
            if use_potion == "1":
                character["Current HP"] = min(character["Current HP"] + 5, character["Max HP"])
                character["Potions"] -= 1
                print(f"Potion used. Current HP: {character['Current HP']}. Potions left: {character['Potions']}.")
            elif use_potion == "2":
                print("You chose not to use a potion.")
            else:
                print("Invalid input. Please enter 1 or 2.")

        win_chance = WIN_CHANCE_BY_LEVEL[character["Level"] - 1]
        xp_change = XP_CHANGE_BY_LEVEL[character["Level"] - 1]
        hp_change = HP_CHANGE_BY_LEVEL[character["Level"] - 1]
        if random.random() < win_chance:
            print(f"You won the battle! XP + {xp_change}, HP + {hp_change}")
            character["XP"] += xp_change
            character["Current HP"] = min(character["Current HP"] + hp_change, character["Max HP"])
        else:
            print(f"You lost the battle. HP - {hp_change}")
            character["Current HP"] -= hp_change
            if character["Current HP"] <= 0:
                print("Game Over. Pikachu has fainted.")
                return False
    elif encounter_chance < 3:
        guess_name = GUESS_GAME_NAME[character["Level"] - 1]
        print(f"You encountered a {guess_name}!")
        guess_range = GUESS_GAME_RANGE[character["Level"] - 1]
        random_number = random.randint(1, guess_range)
        while True:
            try:
                print(f"There is a random number generated in [1 to {guess_range}]")
                user_input = int(input("Please guess, what is the number: ").strip())
            except ValueError:
                print(f"Invalid input: Please enter a number.")
            else:
                if 1 <= user_input <= guess_range:
                    print("You guessing:", user_input)
                    xp_change = GUESS_GAME_XP_CHANGE_BY_LEVEL[character["Level"] - 1]
                    hp_change = GUESS_GAME_HP_CHANGE_BY_LEVEL[character["Level"] - 1]
                    if user_input == random_number:
                        character["XP"] += xp_change
                        character["Current HP"] = min(character["Current HP"] + hp_change, character["Max HP"])
                        print(f"Your guessing is correct, {random_number}! XP + {xp_change}, HP + {hp_change}")
                    else:
                        character["Current HP"] -= hp_change
                        print(f"Your guessing is wrong! Correct number is {random_number}. HP - {hp_change}")
                        if character["Current HP"] <= 0:
                            print("Game Over. Pikachu has fainted.")
                            return False
                    break
                else:
                    print(f"The number is not in the valid range [1 to {guess_range}]")
    else:
        print("No foes encountered this time.")
    return True


def check_level_up(character: dict) -> None:
    level = character["Level"]
    if level < 3 and character["XP"] >= LEVEL_UP_EXPERIENCE[level - 1]:
        character["Level"] += 1
        character["Max HP"] = MAX_HP_BY_LEVEL[level]
        character["Current HP"] = character["Max HP"]
        character["Ability"] = ABILITY_BY_LEVEL[level]
        print(f'Pikachu has leveled up to Level {level + 1}! Ability upgrades to {character["Ability"]}.')


def print_congratulations() -> None:
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


def final_boss_battle(character: dict) -> bool:
    boss_hp = 50
    print("The final boss battle begins!")
    round_number = 0
    while boss_hp > 0 and character["Current HP"] > 0:
        round_number += 1
        print(f"Round {round_number}:")
        player_hit_chance = BOSS_BATTLE_HIT_CHANCE
        if random.random() < player_hit_chance:
            boss_hp -= BOSS_BATTLE_HP_REDUCE[0]
            print(f"You hit the boss! Boss's HP is now {boss_hp}.")
        else:
            print("You missed!")
        if boss_hp > 0:
            character["Current HP"] -= BOSS_BATTLE_HP_REDUCE[1]
            print(f"The boss hit you! Your HP is now {character['Current HP']}.")
        if character["Current HP"] <= 0:
            print("Game Over. Pikachu has fainted.")
            return False
    print_congratulations()
    return True


def game():
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
                if (character["X-coordinate"], character["Y-coordinate"]) == (ROWS - 1, COLUMNS - 1) and character["Level"] >= 3 and character["XP"] >= BOSS_BATTLE_XP_NEED:
                    if final_boss_battle(character):
                        print("Congratulations! Pikachu completes the game!")
                        return
                    else:
                        print("Pikachu is beaten by the final boss. Game over.")
                        return
                else:
                    if not encounter_foe(character):
                        break
            else:
                print("Move not possible. Choose a different direction or meet the requirements to face the boss.")
            check_level_up(character)
        else:
            print("Invalid move. Please choose a different direction.")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
