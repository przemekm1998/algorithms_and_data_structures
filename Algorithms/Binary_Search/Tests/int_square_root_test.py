import unittest
from Algorithms.Binary_Search.int_square_root import IntSquareRoot


class TestIntSquareRoot(unittest.TestCase):
    def test_calc_root(self):
        k = 300
        result = IntSquareRoot.calc_root(k)
        self.assertEqual(result, 17)


if __name__ == '__main__':
    unittest.main()
