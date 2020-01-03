import unittest
from Algorithms.Binary_Search.binary_search import BinarySearch


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.data_input = [2, 5, 6, 7, 8, 8, 9]

    def test_binary_search_above_range(self):

        target = 99
        result = BinarySearch.binary_search_iterative(self.data_input, target)
        self.assertEqual(result, 9)

    def test_binary_search_below_range(self):

        target = -50
        result = BinarySearch.binary_search_iterative(self.data_input, target)
        self.assertEqual(result, 2)

    def test_binary_search_in_array(self):

        target = 6
        result = BinarySearch.binary_search_iterative(self.data_input, target)
        self.assertEqual(result, 6)

    def test_binary_search_in_array_range(self):

        target = 4
        result = BinarySearch.binary_search_iterative(self.data_input, target)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
