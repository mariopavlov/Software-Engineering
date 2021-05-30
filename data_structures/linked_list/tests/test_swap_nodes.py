import unittest
from data_structures.linked_list.src.linked_list import LinkedList, swap_nodes


class SwapNodesTests(unittest.TestCase):
    def test_swap_2_and_4(self):
        arr = [0, 1, 2, 3, 4, 5, 6, 7]
        left = 2
        right = 4
        result =
        expected = [0, 1, 4, 3, 2, 5, 6, 7]
        self.assertEqual(True, False)

    def test_swap_0_and_1(self):
        arr = [3, 4, 5, 2, 6, 1, 9]
        left = 0
        right = 1
        result =
        expected = [1, 0, 2, 3, 4, 5, 6, 7]
        pass

    def test_swap_0_and_0(self):
        """ Testing edge case where the two index elements are the same
            Guessing that it should be handles by the case where I check
            if first index is bigger than second
        """
        arr = [0, 1, 2, 3, 4, 5, 6, 7]
        left = 0
        right = 0
        result =
        expected = None
        pass

    def test_swap_3_and_4(self):
        arr = [0, 1, 2, 3, 4, 5, 6, 7]
        left = 3
        right = 4
        result =
        expected = [0, 1, 2, 4, 3, 5, 6, 7]
        pass

    def test_swap_out_of_size(self):
        """ Testing edge case where I provide second index to swap larger than the List size"""
        arr = [0, 1, 2, 3, 4, 5, 6, 7]
        left = 3
        right = 8
        result =
        expected = None
        pass

    def test_negative_index(self):
        """ Testing negative index
            Explicitly set the first index to negative, because otherwise I can test another if statement with
            which guards different edge case (the case where the second element is less than first)
        """
        arr = [0, 1, 2, 3, 4, 5, 6, 7]
        left = -1
        right = 3
        result =
        expected = None
        pass


if __name__ == '__main__':
    unittest.main()
