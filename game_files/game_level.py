from game_files import LEVEL_UP_EXPERIENCE, MAX_HP_BY_LEVEL
from game_files import ABILITY_BY_LEVEL


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
