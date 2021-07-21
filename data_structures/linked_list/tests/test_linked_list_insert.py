import unittest
from data_structures.linked_list.src.linked_list import LinkedList


class LinkedListInsertTests(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList(1)

    def test_insert_at_0(self):
        self.linked_list.insert(11, 0)

        self.assertEqual([11, 1], self.linked_list.to_list())

    def test_insert_at_13(self):
        """ List contains less than 13 elements, the element should be
        appended at the end of the list"""
        self.linked_list.insert(11, 0)
        self.linked_list.insert(10, 13)

        self.assertEqual([11, 1, 10], self.linked_list.to_list())

    def test_insert_at_1(self):
        self.linked_list.insert(11, 0)
        self.linked_list.insert(10, 13)
        self.linked_list.insert(99, 1)

        self.assertEqual([11, 99, 1, 10], self.linked_list.to_list())


if __name__ == '__main__':
    unittest.main()
