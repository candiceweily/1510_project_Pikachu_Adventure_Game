import itertools

from game_files import ROWS, COLUMNS
from game_files import BOSS_BATTLE_XP_NEED


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
    color_reset = "\033[0m"

    for row, column in itertools.product(range(10), repeat=2):
        if column == 0:
            print("|", end="")
        if (row, column) == (character['X-coordinate'], character['Y-coordinate']):
            print(f" {yellow_start}⚡{color_reset}  |", end="")
        elif (row, column) == (9, 9):
            print(f" 👹 |", end="")
        else:
            print("    |", end="")

        if column == 9:
            print("\n+" + "----+" * 10)


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

