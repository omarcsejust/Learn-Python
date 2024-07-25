from singly_linked_list import Node, create_singly_linked_list, traverse_ll

def insert_at_first(head: Node) -> Node:
    val = int(input("Enter a value: "))
    node = Node()
    node.val = val
    node.next = head
    return node


def insert_at_position(head) -> None:
    position = int(input("Enter a position: "))
    val = int(input("Enter a value: "))
    cur_node = head
    i = 0
    while cur_node:
        i += 1
        if position == i:
            new_node = Node()
            new_node.val = val
            temp = cur_node.next
            cur_node.next = new_node
            new_node.next = temp
            return
        cur_node = cur_node.next


def insert_at_end(head) -> None:
    val = int(input("Enter a value: "))
    cur_node = head
    while cur_node.next:
        cur_node  = cur_node.next

    node = Node()
    node.val = val
    cur_node.next = node


if __name__ == "__main__":
    head = create_singly_linked_list()
    traverse_ll(head)

    head = insert_at_first(head)
    traverse_ll(head)

    insert_at_position(head)
    traverse_ll(head)

    insert_at_end(head)
    traverse_ll(head)


