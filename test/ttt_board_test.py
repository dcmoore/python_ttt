import unittest
from src.ttt_board import TTTBoard

class TestBoard(unittest.TestCase):
  def setUp(self):
    self.board = TTTBoard(9)

  def test_name(self):
    self.assertEqual('TTTBoard', TTTBoard.__name__)
  
  def test_has_an_X_attr(self):
    self.assertEqual('X', self.board.X)

  def test_has_an_O_attr(self):
    self.assertEqual('O', self.board.O)

  def test_has_an_empty_board_by_default(self):
    self.assertEqual(0, self.board.num_moves_made())
  
  def test_can_make_moves_on_the_board(self):
    self.board.make_move(1, self.board.X)
    self.assertEqual(1, self.board.num_moves_made())
    self.board.make_move(0, self.board.O)
    self.assertEqual(2, self.board.num_moves_made())
  
  def test_can_only_make_move_with_X_or_O(self):
    try:
      self.board.make_move(1, 'invalid')
    except Exception as err:
      self.assertEqual('BoardError', err.__class__.__name__)
      self.assertRegex(err.args[0], 'Invalid Team')
    else:
      self.fail('BoardError not thrown when it should be')
  
  def test_can_only_make_moves_from_0_to_one_less_than_the_num_spaces_on_the_board(self):
    try:
      self.board.make_move(-1, self.board.X)
    except Exception as err:
      self.assertEqual('BoardError', err.__class__.__name__)
      self.assertRegex(err.args[0], 'Invalid Move')
    else:
      self.fail('BoardError not thrown when it should be')

    try:
      self.board.make_move(9, self.board.X)
    except Exception as err:
      self.assertEqual('BoardError', err.__class__.__name__)
      self.assertRegex(err.args[0], 'Invalid Move')
    else:
      self.fail('BoardError not thrown when it should be')

  def test_can_only_make_move_at_an_empty_space(self):
    space = 1
    try:
      self.board.make_move(space, self.board.X)
      self.board.make_move(space, self.board.O)
    except Exception as err:
      self.assertEqual('BoardError', err.__class__.__name__)
      self.assertRegex(err.args[0], "Space '{0}' is already full".format(space))
    else:
      self.fail('BoardError not thrown when it should be')
  
  def test_can_retrieve_space_contents(self):
    self.assertEqual('', self.board.space_contents(0), "We haven't set the space yet")
    self.board.make_move(0, self.board.O)
    self.assertEqual('O', self.board.space_contents(0), "After we made a move")