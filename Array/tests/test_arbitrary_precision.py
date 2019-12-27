import unittest
from Array.arbitrary_precision import ArbitraryPrecision


class TestArbitraryPrecision(unittest.TestCase):
    def test_increment_digit_3_digits(self):
        """ Basic test with one carry """

        digit = [1, 4, 9]
        result = ArbitraryPrecision.increment_digit(digit)
        self.assertEqual(result, [1, 5, 0])

    def test_increment_digit_4_digits(self):
        """ Case when array needs to extend """

        digit = [9, 9, 9]
        result = ArbitraryPrecision.increment_digit(digit)
        self.assertEqual(result, [1, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
