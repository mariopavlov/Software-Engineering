import unittest
import sys
import src.concepts.linked_list.merge_list as merge_list
import src.concepts.linked_list.linked_list as linked_list


class MergeListTests(unittest.TestCase):
    def test_empty_lists(self):
        """ Providing two empty lists, we need to receive new empty list """

        for item in sys.path:
            print(f'PATH: {item}')

        list1 = linked_list.LinkedList()
        list2 = linked_list.LinkedList()

        merged_list = merge_list.merge(list1, list2)

        self.assertEqual([], merged_list.to_list())


if __name__ == '__main__':
    unittest.main()
