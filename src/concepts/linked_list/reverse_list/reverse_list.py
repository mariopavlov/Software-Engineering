from src.concepts.linked_list import LinkedList


def reverse(linked_list):
    """ Returns reversed version of a list """
    result = LinkedList()

    for item in linked_list:
        result.prepend(item)

    return result
