# finding the middle node of the linked list

# problem statement: return the middle of the node and if the linked list have even number return the second middle one

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def build_list(values):
    if not values:
        return None
    head = Node(val=values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val=val)
        current = current.next
    return head

def middle_of_linked_list(head:Node) -> int:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow.val


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
    
linkedlist = build_list([1,2,3,4,5,6])

print_linked_list(linkedlist)

print("Middle of linked list is", middle_of_linked_list(linkedlist))