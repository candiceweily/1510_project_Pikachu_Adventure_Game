from game_files import ROWS, COLUMNS
from game_files import BOSS_BATTLE_XP_NEED

from game_files.game_menu import menu, display_help
from game_files.game_board import make_board
from game_files.game_character import make_character, describe_current_location
from game_files.game_navigation import display_map_with_character_position, validate_move, move_character
from game_files.game_progress import get_user_choice
from game_files.game_art import display_welcome_message
from game_files.game_level import check_level_up
from game_files.game_encounters import check_for_encounters
from game_files.game_final_boss import final_boss_battle


def game() -> None:
    """
    Assemble the main game loop for a grid-based adventure game.
    """
    choice = menu()

    if choice == "1":
        display_welcome_message()
        board = make_board(ROWS, COLUMNS)
        character = make_character()
        display_map_with_character_position(character)

        while True:
            describe_current_location(board, character)
            direction = get_user_choice(character)
            if validate_move(character, direction):
                if move_character(character, direction):
                    display_map_with_character_position(character)
                    if (character["X-coordinate"], character["Y-coordinate"]) == (ROWS - 1, COLUMNS - 1):
                        if character["Level"] >= 3 and character["XP"] >= BOSS_BATTLE_XP_NEED:
                            if final_boss_battle(character):
                                print("Congratulations! Pikachu completes the game!")
                                return
                            else:
                                print("Pikachu is beaten by the final boss. Game over.")
                                return
                        else:
                            print("You've reached the final boss location, but you're not ready to fight it. "
                                  "Gain more XP or level up.")
                    else:
                        if not check_for_encounters(character):
                            break
                else:
                    print("Move not possible. Choose a different direction or meet the requirements to face the boss.")
                check_level_up(character)
            else:
                print("Invalid move. Please choose a different direction.")
    elif choice == "2":
        display_help()
        return game()
    elif choice == "3":
        print("Exiting the game. Goodbye!")
        return


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
