import unittest
from src.ttt_game_rules import TTTGameRules
from src.board import Board
from collections import defaultdict

class TestBoard(Board):
  valid_teams_list = ['X', 'O']
  def set_board(self, board_data):
    self._board = defaultdict(str, board_data)

WIN_SETS = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

class TestTTTGameRules(unittest.TestCase):
  def setUp(self):
    self.rules = TTTGameRules(WIN_SETS)
    self.board = TestBoard(9)
    self.X = self.board.valid_teams_list[0]
    self.O = self.board.valid_teams_list[1]

  def test_game_ends_if_the_board_is_full(self):
    self.assertEqual(False, self.rules.is_game_over(self.board))
    self.board.set_board({0: self.X, 1: self.O, 2: self.X, 3: self.O, 4: self.X, 5: self.O, 6: self.X, 7: self.O, 8: self.X})
    self.assertEqual(True, self.rules.is_game_over(self.board))
    
  def test_game_ends_if_a_team_controlls_a_win_set(self):
    self.assertEqual(False, self.rules.is_game_over(self.board))
    self.board.set_board({0: self.X, 1: self.X, 2: self.X})
    self.assertEqual(True, self.rules.is_game_over(self.board))
    self.board.set_board({2: self.O, 4: self.O, 6: self.O})
    self.assertEqual(True, self.rules.is_game_over(self.board))
  
  def test_either_one_team_wins_or_no_teams_win(self):
    self.assertEqual(None, self.rules.get_winner(self.board))
    self.board.set_board({0: self.X, 1: self.X, 2: self.X})
    self.assertEqual(self.X, self.rules.get_winner(self.board))
    self.board.set_board({2: self.O, 4: self.O, 6: self.O})
    self.assertEqual(self.O, self.rules.get_winner(self.board))
    
  def test_X_gets_the_first_turn(self):
    self.assertEqual(self.X, self.rules.active_team(self.board))

  def test_X_and_O_alternate_turns(self):
    self.board.set_board({1: 'X'})
    self.assertEqual(self.O, self.rules.active_team(self.board))
    self.board.set_board({1: 'X', 5: 'O'})
    self.assertEqual(self.X, self.rules.active_team(self.board))  
    
  def test_there_is_no_active_team_if_the_game_is_over(self):
    self.board.set_board({0: self.X, 1: self.O, 2: self.X, 3: self.O, 4: self.X, 5: self.O, 6: self.X, 7: self.O, 8: self.X})
    self.assertEqual(None, self.rules.active_team(self.board))