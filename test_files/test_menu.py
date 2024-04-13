from unittest import TestCase
from unittest.mock import patch
from game_files.game_menu import menu


class TestMenu(TestCase):
    @patch('builtins.input', side_effect=['4', '1'])
    @patch('builtins.print')
    def test_menu_first_invalid_then_valid_input(self, _, __):
        choice = menu()
        self.assertEqual(choice, '1')

    @patch('builtins.input', return_value='1')
    @patch('builtins.print')
    def test_start_game_choice(self, _, __):
        self.assertEqual(menu(), '1')

    @patch('builtins.input', return_value='2')
    @patch('builtins.print')
    def test_help_choice(self, _, __):
        self.assertEqual(menu(), '2')

    @patch('builtins.input', return_value='3')
    @patch('builtins.print')
    def test_exit_game_choice(self, _, __):
        self.assertEqual(menu(), '3')
