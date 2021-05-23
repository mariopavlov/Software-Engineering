""" Incrementing List of digits with 1 (one) and return again List of digits """


def add_one(arr):
    """ Takes number, and returns the incremented result

    @param arr: List of digits (representing number)
    @return: List representing number
    """
    result = []
    
    try:
        number = int(''.join(str(digit) for digit in arr))
        number += 1

        for digit in str(number):
            result.append(digit)
    except ValueError:
        # Handle the exception
        print('Please enter an integer')

    return result
