
def nth_row_pascal(row):
    """
    :param: - n - index (0 based), row that I need to return
    return - list() representing nth row of Pascal's triangle
    """

    triangle = [[1], [1, 1]]

    if row < 0:
        print('Enter valid row number!')
        return None

    if row is 0 or row is 1:
        return triangle[row]

    pass
