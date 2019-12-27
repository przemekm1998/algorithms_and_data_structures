import unittest
from Array.advance_game import ArrayAdvance


class TestArrayAdvance(unittest.TestCase):
    def test_array_advance_winnable(self):
        """ Winnable situation """

        test_array = [3, 3, 1, 0, 2, 0, 1]
        result = ArrayAdvance.array_advance(test_array)
        self.assertEqual(result, True)

    def test_array_advance_unwinnable(self):
        """ Unwinnable situation """

        test_array = [3, 2, 0, 0, 2, 0, 1]
        result = ArrayAdvance.array_advance(test_array)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
