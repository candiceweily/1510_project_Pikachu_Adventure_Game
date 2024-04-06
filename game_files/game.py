import random
from game_files import ROWS, COLUMNS, LEVEL_UP_EXPERIENCE, MAX_HP_BY_LEVEL, FOE_NAMES, WIN_CHANCE_BY_LEVEL
from game_files import GUESS_GAME_NAME, GUESS_GAME_HP_CHANGE_BY_LEVEL, GUESS_GAME_XP_CHANGE_BY_LEVEL, GUESS_GAME_RANGE
from game_files import HP_CHANGE_BY_LEVEL, XP_CHANGE_BY_LEVEL, ABILITY_BY_LEVEL
from game_files import BOSS_BATTLE_XP_NEED, BOSS_BATTLE_HP_REDUCE, BOSS_BATTLE_HIT_CHANCE


def menu():
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


def display_help():
    print("\n--- Help & Information ---")
    print("Welcome to Pikachu Adventure Game!")
    print("Navigate Pikachu through various locations, battle foes, and level up.")
    print("Make strategic decisions to ensure Pikachu's victory.")


def make_board(rows: int, columns: int) -> dict:
    """
    Create a game board with random room descriptions.

    :param rows: a positive integer
    :param columns: a positive integer
    :precondition: rows and columns must be positive integer
    :postcondition: correctly create the game board which each key is a tuple and each value is a string description of
    the room
    :return: the game board as a dictionary
    """
    descriptions = ['Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Hisui']
    return {(row, col): random.choice(descriptions) for row in range(rows) for col in range(columns)}


def make_character() -> dict:
    """
    Create a game character for the game.

    :precondition: character must be a dictionary
    :postcondition: correctly create the character for the game
    :return: the character as a dictionary

    # >>> player_character = make_character()
    # >>> player_character
    # {'Name': 'Pikachu', 'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current HP': 20, 'Max HP': 20, 'XP': 0,
    # 'Ability': 'Thunder Shock', 'Potions': 5}
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
    """
    Describe the current location of the character.

    :param board: board is a non-empty dictionary
    :param character: character is a non-empty dictionary
    :precondition: board is a non-empty dictionary which each key is a tuple and each value is a string description of
    the room
    :precondition: character is a non-empty dictionary that contains location and attributes
    :postcondition: correctly describe the current location of the character

    # >>> player_board = {(0, 0): 'Kanto', (0, 1): 'Johto', (1, 0): 'Hisui', (1, 1): 'Sinnoh'}
    # >>> player_character = {'Name': 'Pikachu', 'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current HP': 20,
    # 'Max HP': 20, 'XP': 0, 'Ability': 'Thunder Shock', 'Potions': 5}
    # >>> describe_current_location(player_board, player_character)
    # You are in Kanto, at location (0, 0).
    #
    # >>> player_board = {(0, 0): 'Kanto', (0, 1): 'Johto', (1, 0): 'Hisui', (1, 1): 'Sinnoh'}
    # >>> player_character = {'Name': 'Pikachu', 'X-coordinate': 1, 'Y-coordinate': 0, 'Level': 1, 'Current HP': 20,
    # 'Max HP': 20, 'XP': 0, 'Ability': 'Thunder Shock', 'Potions': 5}
    # >>> describe_current_location(player_board, player_character)
    You are in Hisui, at location (1, 0).
    """
    location = (character["X-coordinate"], character["Y-coordinate"])
    print(f'You are in {board[location]}, at location {location}.')


def display_map_with_character_position(character: dict) -> None:
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
    """
    Determine if a move in the specified direction is valid.

    :param character: a non-empty dictionary
    :param direction: a non-empty string
    :precondition: character must be a dictionary that contains location and attributes
    :precondition: direction must be one of '1', '2', '3', '4'
    :postcondition: correctly return the boolean result of the position
    :return: return True if the move is valid, otherwise return False

    # >>> validate_move({'X-coordinate': 0, 'Y-coordinate': 0}, '1')
    # False
    # >>> validate_move({'X-coordinate': 2, 'Y-coordinate': 2}, '2')
    # True
    # >>> validate_move({'X-coordinate': 4, 'Y-coordinate': 4}, '3')
    # True
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


def move_character(character: dict, direction: str) -> bool:
    """
    Move the character in a specified direction if possible.

    :param character: a dictionary
    :param direction: a string
    :precondition: character is a non-empty dictionary that contains location and attributes
    :precondition: direction must be one of the strings '1', '2', '3', '4'
    :postcondition: correctly move the character to the given direction
    :return: True if the character's position is successfully updated; False if the move is invalid or the character
    cannot fight the boss due to insufficient level or XP

    # >>> move_character({'X-coordinate': 5, 'Y-coordinate': 5}, '1')
    # True
    # >>> move_character({'X-coordinate': 0, 'Y-coordinate': 0}, '4')
    # True
    # >>> move_character({'X-coordinate': 9, 'Y-coordinate': 9}, '2')
    # True
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


def decide_use_potion(character: dict) -> None:
    if character["Potions"] > 0:
        print(f"Current HP: {character['Current HP']}")
        use_potion = input("Would you like to use a potion before the fight? (1-yes/2-no): ").strip()
        if use_potion == "1":
            character["Current HP"] = min(character["Current HP"] + 5, character["Max HP"])
            character["Potions"] -= 1
            print(f"Potion used. Current HP: {character['Current HP']}. Potions left: {character['Potions']}.")
        elif use_potion != "2":
            print("Invalid input. Please enter 1 or 2.")


def calculate_battle_outcome(character: dict, win_chance: float, xp_change: int, hp_change: int) -> bool:
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


def handle_regular_foe_encounter(character: dict) -> bool:
    foe_name = FOE_NAMES[character["Level"] - 1]
    print(f"You encountered a {foe_name}!")
    decide_use_potion(character)
    win_chance = WIN_CHANCE_BY_LEVEL[character["Level"] - 1]
    xp_change = XP_CHANGE_BY_LEVEL[character["Level"] - 1]
    hp_change = HP_CHANGE_BY_LEVEL[character["Level"] - 1]
    return calculate_battle_outcome(character, win_chance, xp_change, hp_change)


def check_for_encounters(character: dict) -> bool:
    encounter_chance = random.randint(1, 10)
    if encounter_chance > 5:
        return handle_regular_foe_encounter(character)
    else:
        print("No foes encountered this time.")
        return True


def check_level_up(character: dict) -> None:
    """
    Check if the character has enough XP to level up and update the character's level and ability.

    :param character: character is a non-empty dictionary
    :precondition: character is a non-empty dictionary that contains location and attributes
    :postcondition: check if Pikachu has enough XP to level up and correctly update the level and ability
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


def process_battle_round(character: dict, boss_hp: int) -> tuple:
    print(f"Round: ")
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
            return boss_hp, False
    return boss_hp, True


def final_boss_battle(character: dict) -> bool:
    boss_hp = 50
    print("The final boss battle begins!")
    while boss_hp > 0 and character["Current HP"] > 0:
        boss_hp, player_alive = process_battle_round(character, boss_hp)
        if not player_alive:
            return False
    print_congratulations()
    return True


def game():
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
