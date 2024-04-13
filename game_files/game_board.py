import random


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

