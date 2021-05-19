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

