from src.ttt_io import TTTIO

class TerminalTTTIO(TTTIO):
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

  def get_next_move(self):
    return input("Enter your next move: ")
  
  def show_winner(self, winning_team):
    print("Congratulations team: {0}! You won!".format(winning_team))