from unittest import TestCase
from unittest.mock import patch
import io
from game_files.game import describe_current_location, make_board, make_character


class TestDescribeCurrentLocation(TestCase):
    def setUp(self):
        self.board = make_board(10, 10)
        self.character = make_character()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_current_position_at_start(self, mock_stdout):
        self.character['X-coordinate'], self.character['Y-coordinate'] = 0, 0
        describe_current_location(self.board, self.character)
        current_location = (self.character['X-coordinate'], self.character['Y-coordinate'])
        room_description = self.board[current_location]
        expected = f'You are in {room_description}, at location {current_location}.\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_current_position_at_normal(self, mock_stdout):
        self.character['X-coordinate'], self.character['Y-coordinate'] = 4, 6
        describe_current_location(self.board, self.character)
        current_location = (self.character['X-coordinate'], self.character['Y-coordinate'])
        room_description = self.board[current_location]
        expected = f'You are in {room_description}, at location {current_location}.\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_current_position_at_end(self, mock_stdout):
        self.character['X-coordinate'], self.character['Y-coordinate'] = 9, 9
        describe_current_location(self.board, self.character)
        current_location = (self.character['X-coordinate'], self.character['Y-coordinate'])
        room_description = self.board[current_location]
        expected = f'You are in {room_description}, at location {current_location}.\n'
        self.assertEqual(expected, mock_stdout.getvalue())
