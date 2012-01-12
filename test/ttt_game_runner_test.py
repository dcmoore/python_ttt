import unittest
from src.ttt_game_runner import TTTGameRunner
from src.ttt_io import TTTIO

class TestIO(TTTIO):
  def __init__(self):
    self.test_team_inputs = ['Invalid', 'X']
    self.ght_called_count = 0
    self.it_called_count = 0
    
    self.test_move_inputs = ['A', 1, 0, 2]
    self.gnm_called_count = 0
    self.im_called_count = 0
    
    self.sw_called_count = 0
    self.tg_called_count = 0
  
  def get_human_team(self, board):
    team = self.test_team_inputs[self.ght_called_count]
    self.ght_called_count += 1
    return team
  def invalid_team(self):
    self.it_called_count += 1
  def invalid_move(self, message):
    self.im_called_count += 1
  def get_next_move(self):
    move = self.test_move_inputs[self.gnm_called_count]
    self.gnm_called_count += 1
    return move
  def show_winner(self, winner):
    self.sw_called_count += 1
  def tie_game(self):
    self.tg_called_count += 1

class TestAI():
  def __init__(self):
    self.test_ai_moves = [3,4]
    self.gbm_called_count = 0
    
  def get_next_move(self, board, rules):
    move = self.test_ai_moves[self.gbm_called_count]
    self.gbm_called_count += 1
    return move

class TestTTTGameRunner(unittest.TestCase):
  def setUp(self):
    self.runner = TTTGameRunner()
    self.runner.io = TestIO()
    self.runner.ai = TestAI()
  
  def test_asks_for_valid_team_until_one_is_provided(self):
    team = self.runner._get_valid_human_team()
    self.assertEqual(1, self.runner.io.it_called_count)
    self.assertEqual('X', team)
  
  def test_asks_for_valid_move_until_one_is_provided(self):
    self.runner._make_valid_move()
    self.assertEqual(1, self.runner.io.im_called_count)
    self.assertEqual('X', self.runner.board.space_contents(1))
  
  def test_human_and_computer_players_alternate_turns(self):
    self.runner.human_team = 'X'
    self.runner._take_turn('X')
    self.runner._take_turn('O')
    self.assertEqual(2, self.runner.board.num_full_spaces())
    self.assertEqual('X', self.runner.board.space_contents(1))
    self.assertEqual('O', self.runner.board.space_contents(3))
  
  def test_plays_a_game_until_it_is_done(self):
    self.runner.run_game()
    self.assertEqual(5, self.runner.board.num_full_spaces())
    self.assertEqual(1, self.runner.io.sw_called_count)
  
  def test_shows_winner(self):
    self.runner.rules.get_winner = lambda board: 'X'
    self.runner.game_over()
    self.assertEqual(1, self.runner.io.sw_called_count)
    
  def test_shows_tie_game(self):
    self.runner.rules.get_winner = lambda board: None
    self.runner.game_over()
    self.assertEqual(1, self.runner.io.tg_called_count)