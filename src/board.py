from collections import defaultdict

class Board():
  num_spaces = 0
  valid_teams_list = []
  
  def __init__(self, num_spaces):
    self._board = defaultdict(str)
    self.num_spaces = num_spaces
  
  def fill_space(self, location, team):
    self._board[location] = team
  
  def erase_space(self, location):
    if location in self._board: self._board.pop(location)
  
  def space_contents(self, location):
    if location in self._board: return self._board[location]
    return ''
  
  def num_full_spaces(self):
    return len(self._board)

  def to_dict(self):
    return self._board.copy()