import unittest
from data_structures.linked_list.src.linked_list import LinkedList, is_circular


class LinkedListCircular(unittest.TestCase):

    def test_circular_list(self):
        # Test Case initialization
        list_with_loop = LinkedList([2, -1, 3, 0, 5])

        # Creating a loop where the last node points back to the second node
        # loop_start is equal to the second node [-1]
        loop_start = list_with_loop.head.next

        # Iterate over the original list
        node = list_with_loop.head
        while node.next:
            node = node.next

        # We have the last element in the list,
        # create the Loop by setting the last element to point to the second
        node.next = loop_start

        circular = is_circular(list_with_loop)

        self.assertEqual(True, circular)

    def test_non_circular_list(self):
        list_without_loop = LinkedList([2, -1, 3, 0, 5])

        circular = is_circular(list_without_loop)

        self.assertEqual(False, circular)

    def test_empty_list_for_circularity(self):
        empty_list = LinkedList([])

        self.assertEqual(False, is_circular(empty_list))


if __name__ == '__main__':
    unittest.main()
