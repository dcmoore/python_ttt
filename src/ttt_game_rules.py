from src.game_rules import GameRules

class TTTGameRules(GameRules):
  def __init__(self, win_sets):
    self._win_sets = win_sets
    
  def _set_is_controlled_by(self, board, win_set):
    teams_in_set = []
    for space in win_set:
      team_in_space = board.space_contents(space)
      if team_in_space != '': teams_in_set.append(team_in_space)
    if len(set(teams_in_set)) == 1 and len(teams_in_set) == len(win_set): return teams_in_set[0]
    return None
  
  def is_game_over(self, board):
    if board.num_full_spaces() == board.num_spaces: return True
    for win_set in self._win_sets:
      if self._set_is_controlled_by(board, win_set) != None: return True
    return False
  
  def get_winner(self, board):
    for win_set in self._win_sets:
      if self._set_is_controlled_by(board, win_set) != None: return self._set_is_controlled_by(board, win_set)
  
  def active_team(self, board):
    num_moves = board.num_full_spaces()
    if not self.is_game_over(board):
      num_teams = len(board.valid_teams_list)
      return board.valid_teams_list[num_moves % num_teams]
  
  def possible_moves(self, board):
    return board.empty_spaces()