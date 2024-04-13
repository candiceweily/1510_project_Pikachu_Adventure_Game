import random
from game_files import FOE_NAMES, WIN_CHANCE_BY_LEVEL
from game_files import HP_CHANGE_BY_LEVEL, XP_CHANGE_BY_LEVEL

from game_files.game_progress import decide_use_potion


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
