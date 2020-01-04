import unittest
from Algorithms.Binary_Search.first_entry import FirstEntry


class TestFirstEntry(unittest.TestCase):
    def setUp(self):
        self.input_data = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

    def test_entry_of_exist(self):
        """ Existing entry of with duplicate """

        target = 108
        result = FirstEntry.entry_of(self.input_data, target)
        self.assertEqual(result, 3)

    def test_entry_of_edge(self):
        """ Existing entry on the edge of an array """

        target = 401
        result = FirstEntry.entry_of(self.input_data, target)
        self.assertEqual(result, 9)

    def test_entry_of_not_existing(self):
        """ Target is not existing in the array """

        target = 500
        result = FirstEntry.entry_of(self.input_data, target)
        self.assertEqual(result, None)

    def test_entry_of_empty(self):
        """ Empty array case """

        target = 500
        result = FirstEntry.entry_of([], target)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
