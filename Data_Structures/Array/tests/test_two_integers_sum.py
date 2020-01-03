import unittest
from Data_Structures.Array.two_integers_sum import TwoIntegersSum, ThreeIntegersSum


class TestTwoIntegersSum(unittest.TestCase):
    def test_check_found(self):
        """ A pair of integers can be found """

        array = [-2, 1, 2, 4, 7, 11, 2]
        target = 13
        self.assertEqual(TwoIntegersSum.check(array, target), [2, 11])

    def test_check_not_found(self):
        """ A pair of integers can be found """

        array = [-2, 1, 2, 4, 7, 2]
        target = 13
        self.assertEqual(TwoIntegersSum.check(array, target), None)


class TestThreeIntegersSum(unittest.TestCase):
    def test_check_found(self):
        """ Three integers that sum up to 21 can be found """

        array = [3, 1, 7, 4, 5, 9, 10]
        target = 21
        self.assertEqual(ThreeIntegersSum.check(array, target), [4, 7, 10])

    def test_check_not_found(self):
        """ Three integers that sum up to 21 cannot be found """

        array = [3, 1, 7, 4, 5]
        target = 21
        self.assertEqual(ThreeIntegersSum.check(array, target), None)


if __name__ == '__main__':
    unittest.main()
