from unittest import TestCase
from unittest.mock import patch
from game_files.game_progress import decide_use_potion


class TestDecideUsePotion(TestCase):
    @patch('builtins.input', return_value='1')
    def test_use_potion(self, _):
        character = {
            'Name': 'Test Character',
            'Current HP': 15,
            'Max HP': 20,
            'Potions': 3
        }
        decide_use_potion(character)
        self.assertEqual(character['Current HP'], 20)
        self.assertEqual(character['Potions'], 2)

    @patch('builtins.input', return_value='2')
    def test_not_use_potion(self, _):
        character = {
            'Name': 'Test Character',
            'Current HP': 15,
            'Max HP': 20,
            'Potions': 3
        }
        decide_use_potion(character)
        self.assertEqual(character['Current HP'], 15)
        self.assertEqual(character['Potions'], 3)
