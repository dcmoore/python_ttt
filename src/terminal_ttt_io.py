from src.ttt_io import TTTIO

class TerminalTTTIO(TTTIO):
  def get_human_team(self, board):
    return input("Enter your team {0}: ".format(board.valid_teams_list))
    
  def get_next_move(self):
    return input("Enter your next move: ")
  
  def invalid_team(self):
    print("Invalid Team.")
  
  def invalid_move(self, message):
    print(message)
  
  def _board_to_str(self, ttt_board):
    def _space_to_str(space_number):
      space = ttt_board.space_contents(space_number)
      if space == ttt_board.EMPTY_SPACE: return ' '
      return space

    output = "-------\n"
    for row in iter(range(0,ttt_board.num_rows)):
      output += "|"
      for col in iter(range(0,ttt_board.num_cols)):
        space_number = (3 * row) + col
        output += "{0}|".format(_space_to_str(space_number))
      output += "\n-------\n"

    return output
  
  def show_board(self, ttt_board):
    print(self._board_to_str(ttt_board))
    
  def thinking(self):
    print("Please Wait. Thinking of next move...")
  
  def tie_game(self):
    print('Nobody wins... Or as your mother would say, "Everybody Wins!"')
  
  def show_winner(self, winner):
    print("Congratulations {0}! You won!".format(winner))