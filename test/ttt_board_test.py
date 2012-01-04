import unittest
from src.ttt_board import TTTBoard

class TestBoard(unittest.TestCase):
  def test_name(self):
    self.assertEqual('TTTBoard', TTTBoard.__name__)