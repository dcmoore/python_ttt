import unittest
from src.terminal_ttt_io import TerminalTTTIO
from src.ttt_board import TTTBoard

class TestTerminalTTTIO(unittest.TestCase):
  def test_board_gets_displayed_properly(self):
    board = TTTBoard(9)
    io = TerminalTTTIO()
    expected = "-------\n|0|1|2|\n-------\n|3|4|5|\n-------\n|6|7|8|\n-------\n"
    self.assertEqual(expected, io._board_to_str(board))
    
    board.fill_space(0, 'X')
    board.fill_space(7, 'O')
    expected = "-------\n|X|1|2|\n-------\n|3|4|5|\n-------\n|6|O|8|\n-------\n"
    self.assertEqual(expected, io._board_to_str(board))