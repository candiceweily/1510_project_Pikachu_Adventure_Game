def get_user_choice(character: dict[str: str | int]) -> str:
    """
    Prompt the user to make a choice where to move their character or to view their character's current HP or level.

    :param character: a non-empty dictionary
    :precondition: character is a non-empty dictionary that contains location and attributes
    :postcondition: get the choice of the character or display the current HP or level correctly
    :return: the choice of the character as a string
    """
    choices = ["North", "South", "East", "West", "Show Current HP", "Show Current Level"]
    print("Where would you like to go? Or type '5' to see current HP, '6' to see current level.")
    for index, value in enumerate(choices, start=1):
        print(f'{index}: {value}')
    choice = input("Choose a direction (1/2/3/4) or type 5/6: ").strip()
    while choice not in [str(index) for index in range(1, 7)]:
        print("Invalid choice, try again.")
        choice = input("Choose a direction (1/2/3/4) or type 5/6: ").strip()
    if choice == "5":
        print(f"Current HP: {character['Current HP']}/{character['Max HP']}")
    elif choice == "6":
        print(f"Current Level: {character['Level']}")
    else:
        return choice
    return get_user_choice(character)


def decide_use_potion(character: dict[str: str | int]) -> None:
    """
    Prompt the player to decide whether to use a potion to heal the character before a fight.

    :param character: a non-empty dictionary
    :precondition: character is a non-empty dictionary that contains location and attributes
    :postcondition: update the potion data based on the user choice and print the useful information
    """
    if character["Potions"] > 0:
        print(f"Current HP: {character['Current HP']}")
        use_potion = input("Would you like to use a potion before the fight? (1-yes/2-no): ").strip()
        if use_potion == "1":
            character["Current HP"] = min(character["Current HP"] + 5, character["Max HP"])
            character["Potions"] -= 1
            print(f"Potion used. Current HP: {character['Current HP']}. Potions left: {character['Potions']}.")
        elif use_potion != "2":
            print("Invalid input. You lost your chance to use potion")
