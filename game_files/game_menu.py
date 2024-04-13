def menu() -> str:
    """
    Display the main menu for the game and prompt the user to make a choice.

    :postcondition: prompt the user to choose the desired option return the choice from the user
    :return: the choice from the user as a string
    """
    while True:
        print("\n--- Pikachu Adventure Game Menu ---")
        print("1. Start Game")
        print("2. Help")
        print("3. Exit")
        choice = input("Enter your choice (1, 2 or 3): ").strip()
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def display_help() -> None:
    """
    Display the help section for the game.

    :postcondition: print the help section for the game
    """
    print("\n--- Help & Information ---")
    print("Welcome to Pikachu Adventure Game!")
    print("Navigate Pikachu through various locations, battle foes, and level up.")
    print("Make strategic decisions to ensure Pikachu's victory.")

