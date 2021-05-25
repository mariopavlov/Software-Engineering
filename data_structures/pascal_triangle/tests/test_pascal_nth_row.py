import unittest
from data_structures.pascal_triangle.src.pascal_triangle import nth_row_pascal


class PascalTriangleGetRowTests(unittest.TestCase):

    def test_negative_row(self):
        row = nth_row_pascal(-1)
        self.assertEqual(None, row)

    def test_first_row(self):
        row = nth_row_pascal(0)
        expected = [1]

        self.assertEqual(expected, row)

    def test_second_row(self):
        row = nth_row_pascal(1)
        expected = [1, 1]

        self.assertEqual(expected, row)
        pass

    def test_third_row(self):
        row = nth_row_pascal(2)
        expected = [1, 2, 1]

        self.assertEqual(expected, row)

    def test_fourth_row(self):
        row = 3
        expected = [1, 3, 3, 1]

        self.assertEqual(expected, row)

    def test_fifth_row(self):
        row = 4
        expected = [1, 4, 6, 4, 1]

        self.assertEqual(expected, row)


if __name__ == '__main__':
    unittest.main()
