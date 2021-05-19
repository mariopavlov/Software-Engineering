import unittest
from data_structures.linked_list.src.linked_list import LinkedList, reverse


class ReverseListTests(unittest.TestCase):

    def test_reverse(self):
        self.linked_list = LinkedList()
        self.linked_list.create_from_list([1, 2, 3, 4, 5])

        reversed_list = reverse(self.linked_list)

        self.assertEqual([5, 4, 3, 2, 1], reversed_list.to_list())


if __name__ == '__main__':
    unittest.main()
