from unittest import TestCase

from game_files.game_character import make_character
from game_files.game_navigation import move_character


class TestMoveCharacter(TestCase):
    def setUp(self):
        self.character = make_character()

    def test_move_up_valid(self):
        self.character['X-coordinate'], self.character['Y-coordinate'] = 5, 5
        direction = '1'
        expected = True
        actual = move_character(self.character, direction)
        self.assertEqual(expected, actual)
        self.assertEqual((4, 5), (self.character['X-coordinate'], self.character['Y-coordinate']))

    def test_move_down_valid(self):
        self.character['X-coordinate'], self.character['Y-coordinate'] = 5, 5
        direction = '2'
        expected = True
        actual = move_character(self.character, direction)
        self.assertEqual(expected, actual)
        self.assertEqual((6, 5), (self.character['X-coordinate'], self.character['Y-coordinate']))

    def test_move_right_valid(self):
        self.character['X-coordinate'], self.character['Y-coordinate'] = 5, 5
        direction = '3'
        expected = True
        actual = move_character(self.character, direction)
        self.assertEqual(expected, actual)
        self.assertEqual((5, 6), (self.character['X-coordinate'], self.character['Y-coordinate']))

    def test_move_left_valid(self):
        self.character['X-coordinate'], self.character['Y-coordinate'] = 5, 5
        direction = '4'
        expected = True
        actual = move_character(self.character, direction)
        self.assertEqual(expected, actual)
        self.assertEqual((5, 4), (self.character['X-coordinate'], self.character['Y-coordinate']))
