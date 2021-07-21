""" Helper module to hold all Linked List related functions. """
from data_structures.linked_list.src.linked_list import LinkedList


def merge(list1, list2):
    """
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    @param list1: Linked List instance (sorted in ascending order)
    @param list2: Linked List instance (sorted in ascending order)
    """
    result = LinkedList()
    head1 = list1.head
    head2 = list2.head

    while head1 or head2 is not None:
        if head1 is None:
            result.append(head2.value)
            head2 = head2.next
        elif head2 is None:
            result.append(head1.value)
            head1 = head1.next
        elif head1.value < head2.value:
            result.append(head1.value)
            head1 = head1.next
        else:
            result.append(head2.value)
            head2 = head2.next

    return result
