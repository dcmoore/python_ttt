import unittest
from src.ttt_board import TTTBoard

class TestBoard(unittest.TestCase):
  def setUp(self):
    self.board = TTTBoard(9)
  
  def test_has_an_X_attr(self):
    self.assertEqual('X', self.board.X)

  def test_has_an_O_attr(self):
    self.assertEqual('O', self.board.O)

  def test_has_an_empty_board_by_default(self):
    self.assertEqual(0, len(self.board.to_dict()))
  
  def test_can_fill_spaces_on_the_board(self):
    self.board.fill_space(1, self.board.X)
    self.assertEqual({1: self.board.X}, self.board.to_dict())
    self.board.fill_space(0, self.board.O)
    self.assertEqual({1: self.board.X, 0: self.board.O}, self.board.to_dict())
  
  def test_knows_how_many_moves_have_been_made(self):
    self.assertEqual(0, self.board.num_full_spaces())
    self.board.fill_space(1, self.board.X)
    self.assertEqual(1, self.board.num_full_spaces())
  
  def test_can_only_fill_space_with_X_or_O(self):
    try:
      self.board.fill_space(1, 'invalid')
    except Exception as err:
      self.assertEqual('TTTBoardError', err.__class__.__name__)
      self.assertRegex(err.args[0], 'Invalid Team')
    else:
      self.fail('BoardError not thrown when it should be')
  
  def test_can_only_fill_spaces_from_0_to_one_less_than_the_num_spaces_on_the_board(self):
    try:
      self.board.fill_space(-1, self.board.X)
    except Exception as err:
      self.assertEqual('TTTBoardError', err.__class__.__name__)
      self.assertRegex(err.args[0], 'Invalid Move')
    else:
      self.fail('BoardError not thrown when it should be')

    try:
      self.board.fill_space(9, self.board.X)
    except Exception as err:
      self.assertEqual('TTTBoardError', err.__class__.__name__)
      self.assertRegex(err.args[0], 'Invalid Move')
    else:
      self.fail('BoardError not thrown when it should be')

  def test_can_only_fill_space_at_an_empty_space(self):
    space = 1
    try:
      self.board.fill_space(space, self.board.X)
      self.board.fill_space(space, self.board.O)
    except Exception as err:
      self.assertEqual('TTTBoardError', err.__class__.__name__)
      self.assertRegex(err.args[0], "Space '{0}' is already full".format(space))
    else:
      self.fail('BoardError not thrown when it should be')
  
  def test_can_retrieve_space_contents(self):
    self.assertEqual('', self.board.space_contents(0), "We haven't set the space yet")
    self.board.fill_space(0, self.board.O)
    self.assertEqual(self.board.O, self.board.space_contents(0), "After we made a move")
  
  def test_can_retrieve_the_board_in_dict_form(self):
    self.board.fill_space(4, self.board.X)
    self.board.fill_space(2, self.board.O)
    self.assertEqual({4: self.board.X, 2: self.board.O}, self.board.to_dict())
    self.board.fill_space(6, self.board.X)
    self.assertEqual({4: self.board.X, 2: self.board.O, 6: self.board.X}, self.board.to_dict())