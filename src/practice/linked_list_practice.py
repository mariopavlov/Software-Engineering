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






empty_linked = LinkedList()
empty_linked.create_from_list([])

print(f'Circular Loop?: {is_circular(list_with_loop)}')
print("Pass" if is_circular(list_with_loop) else "Fail")                  # Pass
print("Pass" if is_circular(empty_linked) else "Fail")                  # Fail

