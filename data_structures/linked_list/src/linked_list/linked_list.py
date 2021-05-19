class Node:
    def __init__(self, value):
        """ Value can be either integer value or HEAD to another list """
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        """ Init value expects either List head (node element) or integer value. """

        if value is not None:
            if type(value) is int:
                self.head = Node(value)
            else:
                self.head = value
        else:
            self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next

        return out

    def create_from_list(self, python_list=None):
        """ Create linked list from Python List """
        self.head = None
        if python_list:
            for value in python_list:
                self.append(value)

    def prepend(self, value):
        """ Prepend a value to the beginning of the list.
        @param value: expects integer value
        """

        if self.head is None:
            self.head = Node(value)
        else:
            new_element = Node(value)
            new_element.next = self.head
            self.head = new_element

    def append(self, value):
        """ Append new node in the end of a Linked List

        @param value: it can be either integer value, or LinkedList node
        """

        if self.head is None:
            self.head = Node(value)
        else:
            # Iterate over the linked list until we have the tail
            tail = self.head
            while tail.next is not None:
                tail = tail.next

            # Append the new node at the end of current Linked list
            tail.next = Node(value)

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        # I will perform a linear search, not like I have too many options
        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return current_node

    def remove(self, value):
        """ Remove first occurrence of value. """

        if self.head is not None:
            # Check if I need to remove the head value
            if self.head.value == value:
                # If there is only one element in the list
                if self.head.next is None:
                    self.head = None
                    return

                # Remove head
                self.head = self.head.next
                return

            # Remove element that is not head
            current_node = self.head
            next_node = current_node.next

            # Iterate over the list until element is found, or list end is reached
            while next_node is not None:
                if next_node.value == value:
                    # Remove one element
                    # I need to perform it that way because of not having back-link
                    current_node.next = next_node.next
                    return

                # Get next elements in the List
                current_node = current_node.next
                next_node = current_node.next

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head is not None:
            popped_element = self.head

            if self.head.next is None:
                self.head = None

            self.head = self.head.next
            return popped_element.value

        return None

    def insert(self, value, pos):
        """ Insert value at pos position(Zero based) in the list. If pos is larger than the
        length of the list, append to the end of the list. """
        current_position = 0

        # Insert at position 0
        if pos == current_position:
            new_element = Node(value)
            new_element.next = self.head
            self.head = new_element
            return

        current_element = self.head
        while current_element is not None:
            current_position += 1
            if pos == current_position:
                new_element = Node(value)
                new_element.next = current_element.next
                current_element.next = new_element
                return

            if current_element.next is None:
                current_element.next = Node(value)
                return

            current_element = current_element.next

    def size(self):
        """ Return the size or length of the linked list. """
        list_size = 0
        current_node = self.head

        while current_node is not None:
            list_size += 1
            current_node = current_node.next

        return list_size

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])


