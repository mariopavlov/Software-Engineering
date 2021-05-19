import sys
from src.concepts.linked_list import LinkedList
import testing_package



print(f'Path: {sys.path}')

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(1)
linked_list.append(3)
linked_list.append(4)
linked_list.append(3)

print(f'List: {linked_list.to_list()}')

linked_list.remove(1)
print(f'Removing [1]: {linked_list.to_list()}')
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"

linked_list.remove(3)
print(f'Removing [3]: {linked_list.to_list()}')
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

linked_list.remove(3)
print(f'Removing [3]: {linked_list.to_list()}')
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

linked_list.remove(3)
print(f'Trying to remove element that is not in the list [3]: {linked_list.to_list()}')

print(f'Final list: {linked_list.to_list()}')

element = linked_list.pop()
print(f'Pop first element! Value: {element}')
print(f'List after popping first element: {linked_list.to_list()}')

linked_list.insert(11, 0)
print(f'Insert element at position 0: {linked_list.to_list()}')

linked_list.insert(10, 13)
print(f'Insert element at larger than list size pos [13]: {linked_list.to_list()}')

linked_list.insert(99, 1)
print(f'Insert element at [1]: {linked_list.to_list()}')

print(f'List size is: {linked_list.size()}')




reversed_list = reverse(linked_list)
print(f'Reversed list: {reversed_list.to_list()}')


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


# Test Cases
list_with_loop = LinkedList()
list_with_loop.create_from_list([2, -1, 3, 0, 5])

print(f'List after Init: {list_with_loop.to_list()}')

# Creating a loop where the last node points back to the second node
# loop_start is equal to the second node [-1]
loop_start = list_with_loop.head.next

# Iterate over the original list
node = list_with_loop.head
while node.next:
    node = node.next

# We have the last element in the list,
# create the Loop by setting the last element to point to the second
node.next = loop_start

empty_linked = LinkedList()
empty_linked.create_from_list([])

print(f'Circular Loop?: {is_circular(list_with_loop)}')
print("Pass" if is_circular(list_with_loop) else "Fail")                  # Pass
print("Pass" if is_circular(empty_linked) else "Fail")                  # Fail

