import unittest
from data_structures.list.src.list import max_sum_subarray


class MaxSumSubarrayTests(unittest.TestCase):

    def test_list_with_string(self):
        arr = [1, 2, '3']
        result = max_sum_subarray(arr)

        self.assertEqual(None, result)

    def test_empty_list(self):
        arr = []
        result = max_sum_subarray(arr)

        self.assertEqual(0, result)

    def test_scenario_1(self):
        arr = [1, 2, 3, -4, 6]
        result = max_sum_subarray(arr)

        self.assertEqual(8, result)

    def test_scenario_2(self):
        arr = [1, 2, -5, -4, 1, 6]
        result = max_sum_subarray(arr)

        self.assertEqual(7, result)

    def test_scenario_3(self):
        arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
        result = max_sum_subarray(arr)

        self.assertEqual(18, result)


if __name__ == '__main__':
    unittest.main()
