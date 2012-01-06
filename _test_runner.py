import unittest

from test.ttt_board_test import TestTTTBoard
from test.ttt_game_rules_test import TestTTTGameRules
from test.ttt_computer_player_test import TestTTTComputerPlayer

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestTTTBoard))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestTTTGameRules))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestTTTComputerPlayer))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

# Note to self: Run tests from command line with 'python3 -m unittest _test_runner.py'