from collections import defaultdict
class TTTBoard():
  X = "X"
  O = "O"
  def __init__(self, num_spaces): 
    self._board = defaultdict(str)
    self._num_spaces = num_spaces
  
  class BoardError(RuntimeError):
    pass
  
  def validate_move(fn):
    def func(*args):
      self, location, team = args
      self.validate_location(location)
      self.validate_team(team)
      self.validate_empty_space(location)
      return fn(*args)
    return func
    
  def validate_location(self, location):
    if location >= self._num_spaces or location < 0:
      raise self.BoardError("Invalid Move")
    
  def validate_team(self, team):
    if team != self.X and team != self.O:
      raise self.BoardError("Invalid Team")
  
  def validate_empty_space(self, location):
    if self._board[location] != '':
      raise self.BoardError("Space '{0}' is already full".format(location))
  
  @validate_move
  def make_move(self, location, team):
    self._board[location] = team
  
  def space_contents(self, location):
    return self._board[location]
    
  def num_moves_made(self):
    return len(self._board)