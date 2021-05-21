import unittest
from data_structures.linked_list.src.linked_list import LinkedList
from data_structures.linked_list.src.nested_list import NestedList


class NestedListTests(unittest.TestCase):

    def setUp(self):
        """ Prepare basic NestedList for testing """
        self.nested = NestedList()

        list1 = LinkedList([1, 3, 5, 7])
        list2 = LinkedList([2, 4, 6, 8])

        self.nested.append(list1)
        self.nested.append(list2)

    def test_empty_nested_returns_linked_list(self):

        empty_nested = NestedList()
        expected = []

        self.assertEqual(expected, empty_nested.to_list())

    def test_1_nested_list(self):
        """ Test if we only have 1 element, which is Linked List """
        nested = NestedList()
        list1 = LinkedList([1, 2, 3])
        nested.append(list1)

        expected = [1, 2, 3]
        result = nested.flatten().to_list()

        self.assertEqual(expected, result)

    def test_2_nested_lists(self):
        """ Test the most basic variant with 2 nested lists """

        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        result = self.nested.flatten().to_list()

        self.assertEqual(expected, result)

    def test_4_nested_lists(self):
        """ Extend basic NestedList with 2 more nested lists, and test the outcome """
        list3 = LinkedList([9])
        list4 = LinkedList([10])

        self.nested.append(list3)
        self.nested.append(list4)

        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = self.nested.flatten().to_list()

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
