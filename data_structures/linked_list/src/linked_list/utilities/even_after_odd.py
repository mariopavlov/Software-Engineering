from data_structures.linked_list.src.linked_list.linked_list import LinkedList


def even_after_odd(linked_list):
    """ Inplace sorting of Linked List, to produce Even After Odd ordering
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """

    result = LinkedList()
    even_head = None
    even_tail = None
    odd_head = None
    odd_tail = None

    item = linked_list.head

    while item is not None:
        next_elem = item.next

        if item.value % 2 is 0:
            if even_head is None:
                even_head = item
                even_tail = even_head
            else:
                even_tail.next = item
                even_tail = item
        else:
            if odd_head is None:
                odd_head = item
                odd_tail = odd_head
            else:
                odd_tail.next = item
                odd_tail = item

        item.next = None
        item = next_elem

    if odd_head is None:
        result.head = even_head
    else:
        odd_tail.next = even_head
        result.head = odd_head

    return result
