from src.board import Board

class TTTBoard(Board):
  X = "X"
  O = "O"
  
  class TTTBoardError(RuntimeError):
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
    if location >= self.num_spaces or location < 0:
      raise self.TTTBoardError("Invalid Move")
    
  def validate_team(self, team):
    if team != self.X and team != self.O:
      raise self.TTTBoardError("Invalid Team")
  
  def validate_empty_space(self, location):
    if self._board[location] != '':
      raise self.TTTBoardError("Space '{0}' is already full".format(location))
  
  @validate_move
  def fill_space(self, location, team):
    super().fill_space(location, team)