from unittest import TestCase
from game_files.game import make_character


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        expected = {
            'Name': 'Pikachu',
            'X-coordinate': 0,
            'Y-coordinate': 0,
            'Level': 1,
            'Current HP': 20,
            'Max HP': 20,
            'XP': 0,
            'Ability': 'Thunder Shock',
            'Potions': 5
        }
        actual = make_character()
        self.assertEqual(expected, actual)
