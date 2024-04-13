import random
import time

from game_files import BOSS_BATTLE_HP_REDUCE, BOSS_BATTLE_HIT_CHANCE
from game_files.game_art import print_congratulations


def process_battle_round(character: dict[str: str | int], boss_hp: int, round_number: int) -> tuple[int, bool, int]:
    """
    Process a single round of battle between the character and the boss, updating health points accordingly.

    In each round of the battle, this function determines whether the character successfully hits the boss based on a
    predefined hit chance. If successful, the boss's HP is reduced. Regardless of the hit's success, the boss then
    attacks the character, potentially reducing the character's HP. If the character's HP falls to 0 or below, the game
    is over.

    :param character: a non-empty dictionary
    :param boss_hp: an integer
    :param round_number: a positive integer
    :precondition: character is a non-empty dictionary that contains location and attributes
    :precondition: boss_hp is an integer representing the current boss HP
    :precondition: round_number is an integer representing the current round number
    :postcondition: process the battle and update health points accordingly

    :return: a tuple containing the updated boss's HP, a boolean indicating whether the character is still alive, and
    the next round number

    """
    print(f"Round {round_number}:")
    time.sleep(1.5)
    if random.random() < BOSS_BATTLE_HIT_CHANCE:
        boss_hp -= BOSS_BATTLE_HP_REDUCE[0]
        print(f"You hit the boss! Boss's HP is now {boss_hp}.")
    else:
        print("You missed!")
    time.sleep(1.5)
    if boss_hp > 0:
        character["Current HP"] -= BOSS_BATTLE_HP_REDUCE[1]
        print(f"The boss hit you! Your HP is now {character['Current HP']}.")
        time.sleep(1.5)
        if character["Current HP"] <= 0:
            print("Game Over. Pikachu has fainted.")
            return boss_hp, False, round_number
    return boss_hp, True, round_number + 1


def final_boss_battle(character: dict[str: str | int]) -> bool:
    """
    Conduct the final boss battle of the game.

    :param character: a non-empty dictionary
    :precondition: character is a non-empty dictionary that contains location and attributes
    :postcondition: update the character's HP based on battle outcomes, end the battle when either party's HP reaches
    zero or below
    :return: True if the character defeats the boss and survives the battle, False otherwise
    """
    boss_hp = 50
    round_number = 1
    print("The final boss battle begins!")
    while boss_hp > 0 and character["Current HP"] > 0:
        boss_hp, player_alive, round_number = process_battle_round(character, boss_hp, round_number)
        if not player_alive:
            return False
    print_congratulations()
    return True
