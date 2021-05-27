import unittest
from data_structures.linked_list.src.linked_list import LinkedList, skip_delete_elements


class SkipDeleteElementsTests(unittest.TestCase):

    def test_empty_linked_list(self):
        arr = LinkedList()
        result = skip_delete_elements(arr, 0, 0)
        expected = []

        self.assertEqual(expected, result.to_list())

    def test_skip2_delete0(self):
        arr = LinkedList([1, 2, 3, 4, 5])
        i = 2
        j = 0
        result = skip_delete_elements(arr, i, j)
        expected = [1, 2, 3, 4, 5]

        self.assertEqual(expected, result.to_list())

    def test_skip2_delete4(self):
        arr = LinkedList([1, 2, 3, 4, 5])
        i = 2
        j = 4
        expected = [1, 2]
        result = skip_delete_elements(arr, i, j)

        self.assertEqual(expected, result.to_list())

    def test_skip2_delete3(self):
        arr = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        i = 2
        j = 3
        expected = [1, 2, 6, 7, 11, 12]
        result = skip_delete_elements(arr, i, j)

        self.assertEqual(expected, result.to_list())

    def test_skip2_delete2(self):
        arr = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        i = 2
        j = 2
        expected = [1, 2, 5, 6, 9, 10]
        result = skip_delete_elements(arr, i, j)

        self.assertEqual(expected, result.to_list())


if __name__ == '__main__':
    unittest.main()
