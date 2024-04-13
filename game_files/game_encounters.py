import random

from game_files.game_foe import handle_regular_foe_encounter
from game_files.game_mini_games import run_math_quiz, run_treasure_hunt


def check_for_encounters(character: dict[str: str | int]) -> bool:
    """
    Check if the character encounters a challenge and handle the encounter accordingly.

    :param character: a non-empty dictionary
    :precondition: character is a non-empty dictionary that contains location and attributes
    :postcondition: the character's state may be updated based on the outcome if an encounter occurs and print a
    useful message otherwise
    :return: True if the character survives the encounter or if no encounter occurs, False if the character is defeated
    and dies
    """
    encounter_chance = random.randint(1, 10)
    if encounter_chance <= 4:
        return handle_regular_foe_encounter(character)
    elif 4 < encounter_chance <= 8:
        print("Pikachu found a challenge stone inscribed with ancient numerals!")
        xp_gained = run_math_quiz()
        if xp_gained > 0:
            character['XP'] += xp_gained
            print(f"Pikachu earns {xp_gained} XP for solving the math challenge!")
    elif 8 < encounter_chance <= 10:
        run_treasure_hunt(character)
    else:
        print("It's a peaceful moment. Nothing special happens.")
    return True