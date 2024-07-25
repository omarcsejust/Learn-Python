class Node:
    def __init__(self) -> None:
        self.val = None
        self.next = None

def create_singly_linked_list() -> Node:
    val = int(input("Enter a value: "))
    if val < 0:
        return
    
    node = Node()
    node.val = val
    node.next = create_singly_linked_list()
    return node


def traverse_ll(head) -> None:
    temp = head
    while temp:
        print("-> ", temp.val)
        temp = temp.next


