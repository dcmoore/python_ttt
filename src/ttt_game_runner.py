from src.ttt_board import TTTBoard
from src.ttt_game_rules import TTTGameRules
from src.terminal_ttt_io import TerminalTTTIO
from src.computer_player import ComputerPlayer

class TTTGameRunner():
  def __init__(self):
    WIN_SETS = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    self.board = TTTBoard(9)
    self.rules = TTTGameRules(WIN_SETS)
    self.io = TerminalTTTIO()
    self.ai = ComputerPlayer()
    
  def _get_valid_human_team(self):
    selected_team = self.io.get_human_team(self.board)
    while not selected_team in self.board.valid_teams_list:
      self.io.invalid_team()
      selected_team = self.io.get_human_team(self.board)
    return selected_team
  
  def _make_valid_move(self):
    try:
      move_location = int(self.io.get_next_move())
      self.board.fill_space(move_location, self.rules.active_team(self.board))
    except Exception as e:
      self.io.invalid_move(e.args[0])
      self._make_valid_move()
  
  def _take_turn(self, current_team):
    if current_team == self.human_team:
      self._make_valid_move()
    if current_team != self.human_team:
      self.io.thinking()
      move_location = self.ai.get_next_move(self.board, self.rules)
      self.board.fill_space(move_location, current_team)

  def run_game(self):
    self.human_team = self._get_valid_human_team()
    
    while not self.rules.is_game_over(self.board):
      self.io.show_board(self.board)
      self._take_turn(self.rules.active_team(self.board))
    
    self.game_over()

  def game_over(self):
    self.io.show_board(self.board)
    winner = self.rules.get_winner(self.board)
    if winner == None: self.io.tie_game()
    if winner != None: self.io.show_winner(winner)