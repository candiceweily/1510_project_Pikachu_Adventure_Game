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

