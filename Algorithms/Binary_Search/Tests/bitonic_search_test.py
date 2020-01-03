import unittest
from Algorithms.Binary_Search.bitonic_peak import BitonicPeak


class TestBitonicPeak(unittest.TestCase):
    def test_bitonic_peak_case_1(self):
        input_data = [1, 6, 5, 4, 3, 2, 1]
        result = BitonicPeak.bitonic_search(input_data)
        self.assertEqual(result, 6)

    def test_bitonic_peak_case_2(self):
        input_data = [1, 2, 3, 4, 5]
        result = BitonicPeak.bitonic_search(input_data)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
