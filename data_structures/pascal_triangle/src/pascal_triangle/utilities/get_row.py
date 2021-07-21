
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

    for i in range(2, row + 1):
        current_row = [1]
        previous_row = triangle[i-1]

        # I'm using as a Range "-1" due to the logic that I use later for taking first and second element
        # I'm always getting one element further and calculating only the middle elements of the Triangle.
        # First and last elements - "1" are added manually.
        for j in range(len(previous_row) - 1):
            first_elem = previous_row[j]
            second_elem = previous_row[j + 1]

            # Every row element is calculation on the previous row elements on top
            current_row.append(first_elem + second_elem)

        current_row.append(1)
        triangle.append(current_row)

    return triangle[row]
