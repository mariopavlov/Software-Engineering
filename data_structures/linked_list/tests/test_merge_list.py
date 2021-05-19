import unittest
import data_structures.linked_list.src.linked_list as linked_list


class MergeListTests(unittest.TestCase):
    def test_empty_lists(self):
        """ Providing two empty lists, we need to receive new empty list """

        list1 = linked_list.LinkedList()
        list2 = linked_list.LinkedList()

        merged_list = linked_list.merge(list1, list2)

        self.assertEqual([], merged_list.to_list())


if __name__ == '__main__':
    unittest.main()
