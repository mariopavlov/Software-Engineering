import unittest
from data_structures.linked_list.src.linked_list import LinkedList, even_after_odd


class MyTestCase(unittest.TestCase):

    def test_empty_linked_list(self):
        arr = LinkedList([])
        expected = []
        solution = even_after_odd(arr)

        self.assertEqual(expected, solution.to_list())

    def test_only_even_numbers(self):
        arr = [2, 4, 6, 8]
        expected = [2, 4, 6, 8]
        solution = even_after_odd(arr)

        self.assertEqual(expected, solution.to_list())

    def test_only_odd_numbers(self):
        arr = [1, 3, 5, 7]
        expected = [1, 3, 5, 7]
        solution = even_after_odd(arr)

        self.assertEqual(expected, solution.to_list())

    def test_odd_even_numbers(self):
        arr = [1, 2, 3, 4, 5, 6]
        expected = [1, 3, 5, 2, 4, 6]
        solution = even_after_odd(arr)

        self.assertEqual(expected, solution.to_list())


if __name__ == '__main__':
    unittest.main()
