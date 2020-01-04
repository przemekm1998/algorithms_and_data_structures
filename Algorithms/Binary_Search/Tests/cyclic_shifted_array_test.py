import unittest
from Algorithms.Binary_Search.cyclic_shifted_array import CyclicShift


class TestCyclicShift(unittest.TestCase):
    def test_find(self):
        A = [4, 5, 6, 7, 1, 2, 3]
        idx = CyclicShift.find(A)
        self.assertEqual(A[idx], 1)


if __name__ == '__main__':
    unittest.main()
