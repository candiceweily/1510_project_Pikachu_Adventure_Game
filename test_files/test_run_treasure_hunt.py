from unittest import TestCase
from unittest.mock import patch
from game_files.game_mini_games import run_treasure_hunt


class TestRunTreasureHunt(TestCase):
    @patch('builtins.input', return_value='1')
    @patch('random.choice', return_value=True)
    def test_treasure_found(self, mock_random, mock_input):
        character = {'Potions': 3}
        self.assertTrue(run_treasure_hunt(character))
        self.assertEqual(character['Potions'], 4)

    @patch('builtins.input', return_value='2')
    def test_no_dig(self, mock_input):
        character = {'Potions': 3}
        self.assertFalse(run_treasure_hunt(character))
        self.assertEqual(character['Potions'], 3)
