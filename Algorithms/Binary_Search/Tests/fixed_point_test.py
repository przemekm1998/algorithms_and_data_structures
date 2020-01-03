import unittest
from Algorithms.Binary_Search.fixed_point import FixedPoint


class TestFixedPoint(unittest.TestCase):
    def test_fixed_point_exists(self):
        """ Fixed point exists """

        input_data = [-10, -5, 0, 3, 7]
        result = FixedPoint.fixed_point(input_data)
        self.assertEqual(result, 3)

    def test_fixed_point_not_exists(self):
        """ Fixed doesnt exist"""

        input_data = [-10, -5, 3, 4, 7, 9]
        result = FixedPoint.fixed_point(input_data)
        self.assertEqual(result, None)

    def test_fixed_point_emtpy_input(self):
        """ Fixed doesnt exist"""

        input_data = []
        result = FixedPoint.fixed_point(input_data)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
