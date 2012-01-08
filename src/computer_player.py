class ComputerPlayer():
  def get_best_move(self, board, rules):
    def _minimax(current_depth, minimax_vals_for_depth):
      if rules.is_game_over(board):
        if rules.get_winner(board) == None:
          return 0
        return -1

      for space in board.empty_spaces():
        board.fill_space(space, rules.active_team(board))
        minimax_vals_for_depth[space] = -1 * _minimax(current_depth+1, {})
        board.erase_space(space)

      best_move = max(minimax_vals_for_depth, key=minimax_vals_for_depth.get)
      if current_depth == 0:
        return best_move
      return minimax_vals_for_depth[best_move]
    
    return _minimax(0, {})