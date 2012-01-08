import unittest
from src.computer_player import ComputerPlayer
from src.board import Board
from src.ttt_game_rules import TTTGameRules
from collections import defaultdict

class TestBoard(Board):
  valid_teams_list = ['X', 'O']
  def set_board(self, board_data):
    self._board = defaultdict(str, board_data)

WIN_SETS = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

class TestComputerPlayer(unittest.TestCase):
  def setUp(self):
    self.comp_player = ComputerPlayer()
    self.board = TestBoard(9)
    self.ttt_rules = TTTGameRules(WIN_SETS)
    self.X = self.board.valid_teams_list[0]
    self.O = self.board.valid_teams_list[1]
  
  def test_makes_a_winning_move_if_it_is_available(self):
    self.board.set_board({0: self.X, 2: self.O, 3: self.O, 4: self.O, 6: self.X, 8: self.X})
    self.assertEqual(7, self.comp_player.get_best_move(self.board, self.ttt_rules))
  
  def test_blocks_an_opponents_winning_move_if_a_winning_move_isnt_available(self):
    self.board.set_board({0: self.X, 4: self.O, 1: self.X})
    self.assertEqual(2, self.comp_player.get_best_move(self.board, self.ttt_rules))
  
  def test_kiddie_corner_trap(self):
    self.board.set_board({0: self.X, 4: self.O, 8: self.X})
    move = self.comp_player.get_best_move(self.board, self.ttt_rules)
    self.assertNotEqual(2, move)
    self.assertNotEqual(6, move)
  
  def test_triangle_trap(self):
    self.board.set_board({0: self.O, 4: self.X, 8: self.X})
    move = self.comp_player.get_best_move(self.board, self.ttt_rules)
    self.assertNotEqual(1, move)
    self.assertNotEqual(3, move)
    self.assertNotEqual(5, move)
    self.assertNotEqual(7, move)
  
  def test_corner_trap(self):
    self.board.set_board({1: self.X, 4: self.O, 5: self.X})
    move = self.comp_player.get_best_move(self.board, self.ttt_rules)
    self.assertNotEqual(3, move)
    self.assertNotEqual(6, move)
    self.assertNotEqual(7, move)

# TODO - make an integration test where all game possibilities are tested out