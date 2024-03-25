import random

LEVEL_UP_EXPERIENCE = [5, 10]
MAX_HP_BY_LEVEL = [20, 30, 50]
ABILITY_BY_LEVEL = ["Thunder Shock", "Thunder Shower", "Thunder Storm"]
FOE_NAMES = ["Junior foe", "Medium foe", "Senior foe"]
WIN_CHANCE_BY_LEVEL = [0.6, 0.7, 0.8]
HP_CHANGE_BY_LEVEL = [1, 2, 3]
XP_CHANGE_BY_LEVEL = [1, 2, 3]
BOSS_BATTLE_XP_NEED = 15
BOSS_BATTLE_HP_REDUCE = [10, 5]
BOSS_BATTLE_HIT_CHANCE = 0.6
ROWS, COLUMNS = 10, 10


def make_board(rows: int, columns: int) -> dict:
    descriptions = ['Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Hisui']
    return {(row, col): random.choice(descriptions) for row in range(rows) for col in range(columns)}


def make_character() -> dict:
    return {"Name": "Pikachu", "X-coordinate": 0, "Y-coordinate": 0, "Level": 1, "Current HP": 20, "Max HP": 20, "XP": 0, "Ability": "Thunder Shock"}


def describe_current_location(board: dict, character: dict) -> None:
    location = (character["X-coordinate"], character["Y-coordinate"])
    print(f'You are in {board[location]}, at location {location}.')


def display_map_with_character_position(character: dict) -> None:
    print('Game Board Map: ')
    print("+" + "----+" * 10)
    red_start = "\033[31m"
    color_reset = "\033[0m"
    for row in range(10):
        print("|", end="")
        for column in range(10):
            if (row, column) == (character['X-coordinate'], character['Y-coordinate']):
                print(f" {red_start}C{color_reset}  |", end="")
            else:
                print("    |", end="")
        print("\n+" + "----+" * 10)


def get_user_choice() -> str:
    choices = {"1": "North", "2": "South", "3": "East", "4": "West"}
    print("Where would you like to go?")
    for key, value in choices.items():
        print(f'{key}: {value}')
    choice = (input("Choose a direction (1/2/3/4): "))
    while choice not in choices:
        print("Invalid choice, try again.")
        choice = (input("Choose a direction (1/2/3/4): "))
    return choice


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


def move_character(character: dict, direction: str) -> None:
    if direction == "1":
        character["X-coordinate"] -= 1
    elif direction == "2":
        character["X-coordinate"] += 1
    elif direction == "3":
        character["Y-coordinate"] += 1
    elif direction == "4":
        character["Y-coordinate"] -= 1


def encounter_foe(character: dict) -> bool:
    encounter_chance = random.randint(1, 10)
    if encounter_chance > 5:
        foe_name = FOE_NAMES[character["Level"] - 1]
        print(f"You encountered a {foe_name}!")
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
                return False
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
            character["Current HP"] -= BOSS_BATTLE_HP_REDUCE[1]  # Assuming each boss hit reduces a fixed amount of player's HP
            print(f"The boss hit you! Your HP is now {character['Current HP']}.")
        if character["Current HP"] <= 0:
            print("Game Over. Pikachu has fainted.")
            return False
    print("Congratulations! You've defeated the final boss and completed the game!")
    return True


def game():
    board = make_board(ROWS, COLUMNS)
    character = make_character()
    display_map_with_character_position(character)
    while True:
        describe_current_location(board, character)
        direction = get_user_choice()
        if validate_move(character, direction):
            move_character(character, direction)
            display_map_with_character_position(character)
            fight_result = encounter_foe(character)
            if not fight_result:
                break
            if character["X-coordinate"] == ROWS - 1 and character["Y-coordinate"] == COLUMNS - 1 and character["Level"] == 3:
                if character["XP"] < BOSS_BATTLE_XP_NEED:
                    print("You've reached the final boss, but you don't have enough XP. Go back and train more.")
                else:
                    if final_boss_battle(character):
                        break
                    else:
                        print("Game Over. You were defeated by the final boss.")
                        break
            check_level_up(character)
        else:
            print("You can't move in that direction.")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
