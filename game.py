import random


def make_board(rows, columns):
    descriptions = ['Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Hisui']
    board = {(row, col): random.choice(descriptions) for row in range(rows) for col in range(columns)}
    return board


def make_character():
    character = {"Name": "Pikachu", "X-coordinate": 0, "Y-coordinate": 0, "Level": 1, "Current HP": 20, "Max HP": 20, "XP":
            0, "Ability": "Thunder Shock"}
    return character


def describe_current_location(board, character):
    location = (character["X-coordinate"], character["Y-coordinate"])
    description = board.get(location)
    hp = character["Current HP"]
    print(f"You are currently in {description} at coordinates {location}, with HP {hp}")


def display_map_with_character_position(character):
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


def get_user_choice():
    directions = {'1': 'North', '2': 'West', '3': 'South', '4': 'East'}
    while True:
        user_direction_input = input('Please select your direction:')
        if user_direction_input.isdigit():
            user_direction_choice = int(user_direction_input)
            if user_direction_choice in directions:
                return directions[user_direction_choice]
            else:
                print('Invalid number choice, please try again!')
        else:
            print('Invalid input. Please enter a number representing the direction.')