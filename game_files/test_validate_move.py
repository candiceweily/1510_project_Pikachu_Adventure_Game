from unittest import TestCase
from game_files.game import validate_move, make_character


class TestValidateMove(TestCase):
    def setUp(self):
        self.character = make_character()

    def test_move_up_from_top_edge(self):
        self.character['X-coordinate'], self.character['Y-coordinate'] = 0, 5
        direction = '1'
        expected = False
        actual = validate_move(self.character, direction)
        self.assertEqual(expected, actual)

    def test_move_down_within_board(self):
        self.character['X-coordinate'], self.character['Y-coordinate'] = 5, 5
        direction = '2'
        expected = True
        actual = validate_move(self.character, direction)
        self.assertEqual(expected, actual)

    def test_move_right_to_edge(self):
        self.character['X-coordinate'], self.character['Y-coordinate'] = 5, 8
        direction = '3'
        expected = True
        actual = validate_move(self.character, direction)
        self.assertEqual(expected, actual)

    def test_move_left_from_left_edge(self):
        self.character['X-coordinate'], self.character['Y-coordinate'] = 5, 0
        direction = '4'
        expected = False
        actual = validate_move(self.character, direction)
        self.assertEqual(expected, actual)

    def test_move_down_from_bottom_edge(self):
        self.character['X-coordinate'], self.character['Y-coordinate'] = 9, 5
        direction = '2'
        expected = False
        actual = validate_move(self.character, direction)
        self.assertEqual(expected, actual)

    def test_move_right_from_right_edge(self):
        self.character['X-coordinate'], self.character['Y-coordinate'] = 5, 9
        direction = '3'
        expected = False
        actual = validate_move(self.character, direction)
        self.assertEqual(expected, actual)
