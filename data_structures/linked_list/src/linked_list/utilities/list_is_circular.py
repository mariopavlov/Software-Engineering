


def is_circular(linked_list):
    """
    Determine whether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """

    if linked_list.head is None:
        return False

    fast_runner = linked_list.head
    slow_runner = linked_list.head

    while fast_runner.next is not None:
        fast_runner = fast_runner.next.next
        slow_runner = slow_runner.next

        if slow_runner == fast_runner:
            return True

    return False
