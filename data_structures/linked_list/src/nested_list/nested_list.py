from ..linked_list import LinkedList
from ..linked_list import merge


class NestedList(LinkedList):
    """ Linked List it just like regular Linked List but every node can contain another Linked list """

    def flatten(self):
        """ It takes N-numbered Nested List and returns single Linked List """

        result = LinkedList

        if self.head is not None:
            if self.head.next is not None:
                list1 = self.head.value
                list2 = self.head.next.value

                result = merge(list1, list2)
                self.head.next.value = result
                self.head = self.head.next
                self.flatten()

            result = self.head.value

        return result
