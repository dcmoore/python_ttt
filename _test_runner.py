import unittest

from test.ttt_board_test import TestBoard

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBoard))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

# Note to self: Run tests from command line with 'python3 -m unittest _test_runner.py'