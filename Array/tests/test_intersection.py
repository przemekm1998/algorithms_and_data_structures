import unittest
from Array.intersection import Intersection


class TestIntersection(unittest.TestCase):
    def test_intersection_found(self):
        """ An intersection can be found """

        test_array_1 = [2, 3, 3, 5, 7, 11]
        test_array_2 = [3, 3, 7, 15, 31]
        result = Intersection.check(test_array_1, test_array_2)

        self.assertEqual(result, [3, 7])

    def test_intersection_not_found(self):
        """ An intersection cannot be found """

        test_array_1 = [2, 3, 3, 5, 11]
        test_array_2 = [7, 15, 31]
        result = Intersection.check(test_array_1, test_array_2)

        self.assertEqual(result, [])

    def test_intersection_empty_array(self):
        """ One of the arrays is empty """

        test_array_1 = []
        test_array_2 = [7, 15, 31]
        result = Intersection.check(test_array_1, test_array_2)

        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
