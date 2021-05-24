import unittest
from data_structures.list.src.list import duplicate_number


class DuplicateNumberTests(unittest.TestCase):
    def test_empty_list(self):
        arr = []
        solution = duplicate_number(arr)

        self.assertEqual(None, solution)

    def test_non_duplicate_list(self):
        arr = [1, 2, 3, 4, 5, 6]
        solution = duplicate_number(arr)

        self.assertEqual(None, solution)

    def test_with_2_numbers(self):
        arr = [99, 99]
        solution = duplicate_number(arr)

        self.assertEqual(99, solution)

    def test_duplicate_0(self):
        arr = [0, 1, 5, 4, 3, 2, 0]
        solution = duplicate_number(arr)

        self.assertEqual(0, solution)

    def test_duplicate_3(self):
        arr = [0, 2, 3, 1, 4, 5, 3]
        solution = duplicate_number(arr)

        self.assertEqual(3, solution)

    def test_duplicate_5(self):
        arr = [0, 1, 5, 5, 3, 2, 4]
        solution = duplicate_number(arr)

        self.assertEqual(5, solution)


if __name__ == '__main__':
    unittest.main()
