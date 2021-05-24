

def duplicate_number(arr):
    """ Check List of Integer elements for duplicate number, and returns the value if found

    @param arr: Python list of numbers
    @return: None if no duplicate number is found, Integer if duplicate number is found
    """

    temp = set()

    for num in arr:
        if num in temp:
            return num
        else:
            temp.add(num)

    return None
