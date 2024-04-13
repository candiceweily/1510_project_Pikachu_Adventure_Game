from unittest import TestCase
from unittest.mock import patch
import io

from game_files.game_progress import get_user_choice
from game_files.game_character import make_character


class TestGetUserChoice(TestCase):
    def setUp(self):
        self.character = make_character()

    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_direction_north(self, _, __):
        direction = get_user_choice(self.character)
        self.assertEqual('1', direction)

    @patch('builtins.input', side_effect=['2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_direction_south(self, _, __):
        direction = get_user_choice(self.character)
        self.assertEqual('2', direction)

    @patch('builtins.input', side_effect=['3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_direction_number(self, _, __):
        direction = get_user_choice(self.character)
        self.assertEqual('3', direction)

    @patch('builtins.input', side_effect=['4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_direction_number(self, _, __):
        direction = get_user_choice(self.character)
        self.assertEqual('4', direction)

    @patch('builtins.input', side_effect=['9', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_number_then_valid(self, _, __):
        direction = get_user_choice(self.character)
        self.assertEqual('2', direction)

    @patch('builtins.input', side_effect=['a', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_non_numeric_then_valid(self, _, __):
        direction = get_user_choice(self.character)
        self.assertEqual('3', direction)

    @patch('builtins.input', side_effect=['5', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_choice_number_five(self, mock_stdout, __):
        get_user_choice(self.character)
        current_hp = self.character['Current HP']
        max_hp = self.character['Max HP']

        prompts = ("Where would you like to go? Or type '5' to see current HP, '6' to see current level.\n"
                   "1: North\n"
                   "2: South\n"
                   "3: East\n"
                   "4: West\n"
                   "5: Show Current HP\n"
                   "6: Show Current Level\n")
        expected_output = prompts + f"Current HP: {current_hp}/{max_hp}\n" + prompts

        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['6', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_choice_number_six(self, mock_stdout, __):
        get_user_choice(self.character)
        current_level = self.character['Level']

        prompts = ("Where would you like to go? Or type '5' to see current HP, '6' to see current level.\n"
                   "1: North\n"
                   "2: South\n"
                   "3: East\n"
                   "4: West\n"
                   "5: Show Current HP\n"
                   "6: Show Current Level\n")
        expected_output = prompts + f"Current Level: {current_level}\n" + prompts

        self.assertEqual(expected_output, mock_stdout.getvalue())
