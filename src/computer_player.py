class ComputerPlayer():
  def random_move(self, low, high, rules, board):
    import random
    move = random.randint(low, high)
    return rules.possible_moves(board)[move]
  
  def get_next_move(self, board, rules):
    max_depth = 7
    def _minimax(current_depth, minimax_vals_for_depth):
      if current_depth >= max_depth: return 0
      if rules.is_game_over(board):
        if rules.get_winner(board) == None:
          return 0
        return -1

      for space in rules.possible_moves(board):
        board.fill_space(space, rules.active_team(board))
        minimax_vals_for_depth[space] = -1 * _minimax(current_depth+1, {})
        board.erase_space(space)

      best_move = max(minimax_vals_for_depth, key=minimax_vals_for_depth.get)
      if current_depth == 0:
        return best_move
      return minimax_vals_for_depth[best_move]
      
    if board.num_full_spaces() == 0: return self.random_move(0, len(rules.possible_moves(board))-1, rules, board)
    return _minimax(0, {})