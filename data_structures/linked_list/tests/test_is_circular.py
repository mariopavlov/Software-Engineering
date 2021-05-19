import unittest
from data_structures.linked_list.src.linked_list import LinkedList, is_circular


class LinkedListCircular(unittest.TestCase):

    def test_circular_list(self):
        list_with_loop = LinkedList()
        list_with_loop.create_from_list([2, -1, 3, 0, 5])
        self.assertEqual(True, False)

    def test_non_circular_list(self):
        list_without_loop = LinkedList([2, -1, 3, 0, 5])
        print(list_without_loop.to_list())

        circular = is_circular(list_without_loop)

        self.assertEqual(False, circular)


if __name__ == '__main__':
    unittest.main()
