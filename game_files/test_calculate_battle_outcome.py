from unittest import TestCase
from unittest.mock import patch
from game_files.game import calculate_battle_outcome


class TestCalculateBattleOutcome(TestCase):
    @patch('game_files.game.random.random', return_value=0.2)
    @patch('builtins.print')
    def test_win_battle(self, _, __):
        character = {'XP': 0, 'Current HP': 10, 'Max HP': 20}
        win_chance = 0.5
        xp_change = 10
        hp_change = 5
        result = calculate_battle_outcome(character, win_chance, xp_change, hp_change)
        self.assertTrue(result)
        self.assertEqual(character['XP'], 10)
        self.assertEqual(character['Current HP'], 10)

    @patch('game_files.game.random.random', return_value=0.8)
    @patch('builtins.print')
    def test_lose_battle_game_over(self, _, __):
        character = {'XP': 0, 'Current HP': 5, 'Max HP': 20}
        win_chance = 0.5
        xp_change = 10
        hp_change = 10
        result = calculate_battle_outcome(character, win_chance, xp_change, hp_change)
        self.assertFalse(result)
        self.assertLessEqual(character['Current HP'], 0)

    @patch('game_files.game.random.random', return_value=0.4)
    @patch('builtins.print')
    def test_win_battle_no_level_up(self, _, __):
        character = {'XP': 5, 'Current HP': 15, 'Max HP': 20}
        win_chance = 0.5
        xp_change = 3
        hp_change = 5
        result = calculate_battle_outcome(character, win_chance, xp_change, hp_change)
        self.assertTrue(result)
        self.assertEqual(character['XP'], 8)
        self.assertEqual(character['Current HP'], 15)
