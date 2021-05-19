import unittest
from data_structures.linked_list.src.linked_list import LinkedList


class LinkedListTests(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(1)
        self.linked_list.append(3)
        self.linked_list.append(4)
        self.linked_list.append(3)

    def test_list_append(self):
        self.assertEqual([1, 2, 1, 3, 4, 3], self.linked_list.to_list())

    def test_remove_1_element(self):
        self.linked_list.remove(1)
        self.assertEqual([2, 1, 3, 4, 3], self.linked_list.to_list())

    def test_remove_2_elements(self):
        self.linked_list.remove(1)
        self.linked_list.remove(1)
        self.assertEqual([2, 3, 4, 3], self.linked_list.to_list())

    def test_pop_element(self):
        top_element = self.linked_list.pop()
        self.assertEqual(1, top_element)
        self.assertEqual([2, 1, 3, 4, 3], self.linked_list.to_list())

    def test_list_size(self):
        self.assertEqual(6, self.linked_list.size())


if __name__ == '__main__':
    unittest.main()
