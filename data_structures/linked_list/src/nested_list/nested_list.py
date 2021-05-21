from ..linked_list import LinkedList
from ..linked_list import merge


class NestedList(LinkedList):
    """ Linked List it just like regular Linked List but every node can contain another Linked list """

    def flatten(self):
        """ """
        list1 = self.head.value
        list2 = self.head.next.value

        result = merge(list1, list2)

        return result
