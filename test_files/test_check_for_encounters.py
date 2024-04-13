from unittest import TestCase
from unittest.mock import patch
from game_files.game import check_for_encounters


class TestCheckForEncounters(TestCase):

    @patch('game_files.game.random.randint', return_value=4)
    @patch('game_files.game.print')
    def test_no_encounter(self, mock_print, _):
        character = {'Level': 1, 'XP': 0, 'Current HP': 10, 'Max HP': 20}
        result = check_for_encounters(character)
        self.assertTrue(result)
        mock_print.assert_called_once_with("No foes encountered this time.")

    @patch('game_files.game.random.randint', return_value=6)
    @patch('game_files.game.handle_regular_foe_encounter', return_value=True)
    def test_encounter_and_win(self, mock_handle_foe, _):
        character = {'Level': 1, 'XP': 0, 'Current HP': 10, 'Max HP': 20}
        result = check_for_encounters(character)
        self.assertTrue(result)
        mock_handle_foe.assert_called_once()

    @patch('game_files.game.random.randint', return_value=10)
    @patch('game_files.game.handle_regular_foe_encounter', return_value=False)
    def test_encounter_and_lose(self, mock_handle_foe, _):
        character = {'Level': 1, 'XP': 0, 'Current HP': 10, 'Max HP': 20}
        result = check_for_encounters(character)
        self.assertFalse(result)
        mock_handle_foe.assert_called_once()
