import unittest
from data_structures.linked_list.src.linked_list import Node, LinkedList, merge


class MergeListTests(unittest.TestCase):
    def test_empty_lists(self):
        """ Providing two empty lists, we need to receive new empty list """

        list1 = LinkedList()
        list2 = LinkedList()

        merged_list = merge(list1, list2)

        self.assertEqual([], merged_list.to_list())

    def test_two_lists(self):
        """ Tests that two lists are merged and they are sorted out (input should be sorted) """
        list1 = LinkedList(1)
        list1.append(3)
        list1.append(5)

        list2 = LinkedList(Node(2))
        list2.append(4)

        merged_list = merge(list1, list2)
        print(merged_list.to_list())

        self.assertEqual([1, 2, 3, 4, 5], merged_list.to_list())


if __name__ == '__main__':
    unittest.main()
