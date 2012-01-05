import unittest

from test.ttt_board_test import TestBoard
from test.ttt_game_rules_test import TestGameRules

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBoard))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestGameRules))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

# Note to self: Run tests from command line with 'python3 -m unittest _test_runner.py'