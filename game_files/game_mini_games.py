import random


def run_math_quiz() -> int:
    """
    Conducts a simple math quiz where the user is asked to solve a math problem.
    The character earns XP based on the correctness of the answer.

    :return: The amount of XP earned, 5 for a correct answer and 0 for an incorrect answer
    """
    num1, num2 = random.randint(1, 10), random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    correct_answer = eval(f"{num1} {operation} {num2}")
    print(f"Solve this math problem: {num1} {operation} {num2}")
    while True:
        try:
            player_answer = int(input("Enter your answer: "))
            if player_answer == correct_answer:
                print("Correct! Pikachu gains 5 bonus XP!")
                return 5
            else:
                print("Oops! That's not right. The correct answer was:", correct_answer)
                return 0
        except ValueError:
            print("Invalid number, try again.")


def run_treasure_hunt(character: dict[str, str | int]) -> bool:
    """
    Offers the user a choice to dig for treasure, potentially increasing the potion count.

    :param character: character is a non-empty dictionary
    :precondition: character is a non-empty dictionary that contains location and attributes
    :return: True if a treasure was found and dug up, False otherwise
    """
    print("Pikachu has stumbled upon a suspicious-looking patch of ground.")
    decision = input("Do you want Pikachu to dig here? (1-yes/2-no): ").strip()
    while decision not in ['1', '2']:
        decision = input("Invalid input. Enter 1 for yes or 2 for no: ").strip()
    if decision == '1':
        if random.choice([True, False]):
            character['Potions'] += 1
            print(f"Congratulations! Found a treasure! Potions now: {character['Potions']}.")
            return True
        else:
            print("No treasure here. Better luck next time!")
            return False
    print("Pikachu decides not to dig.")
    return False
