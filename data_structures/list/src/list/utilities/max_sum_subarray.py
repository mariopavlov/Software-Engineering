

def max_sum_subarray(arr):
    """ Looking for maximum continuous sum inside list of numbers that is not separated with sub-array.
    Sub-array is created when single element is higher than the current sum of the sub-array + element itself.

    @param arr: List of numbers (negative and positive)
    @return: Maximum sum inside the number that is not separated from Sub-array
    """
    current_sum = 0
    max_sum = 0

    for element in arr:
        try:
            current_sum = max(current_sum + element, element)
            max_sum = max(current_sum, max_sum)
        except TypeError:
            print('Input List is not in correct format. Please submit only numerical elements!')
            return None

    return max_sum
