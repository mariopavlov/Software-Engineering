from ..linked_list import LinkedList


def skip_delete_elements(linked_list, i, j):
    """ Iterate over Linked List, skip 'i' elements, and delete 'j' elements

    We are iterating over a Linked List (over all elements), by skipping a 'i' number of elements,
    then after that number of skipped elements we are deleting the next 'j' elements.
    When the original list is iterated, newly created instance is returned.

    @param linked_list: Input Linked List that will be iterated to get elements
    @param i: Skip next 'i' elements
    @param j: Delete next 'j' elements
    @return: LinkedList() instance that holds the skip elements
    """
    skip_count = i
    delete_count = j
    result = LinkedList()

    return result
