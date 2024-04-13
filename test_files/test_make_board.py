from unittest import TestCase
from game_files.game_board import make_board


class TestMakeBoard(TestCase):
    def test_make_board_size(self):
        rows, columns = 10, 10
        board = make_board(rows, columns)
        self.assertEqual(len(board), rows * columns)

    def test_make_board_keys(self):
        rows, columns = 10, 10
        board = make_board(rows, columns)
        expected_keys = {(row, col) for row in range(rows) for col in range(columns)}
        self.assertEqual(set(board.keys()), expected_keys)

    def test_make_board_values(self):
        rows, columns = 10, 10
        descriptions = ['Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Hisui']
        board = make_board(rows, columns)
        all_descriptions_valid = all(value in descriptions for value in board.values())
        self.assertTrue(all_descriptions_valid)
