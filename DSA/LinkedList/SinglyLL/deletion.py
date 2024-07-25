from singly_linked_list import Node, create_singly_linked_list, traverse_ll

def delete_first_node(head) -> None:
    return head.next

def delete_nth_node(head):
    position = int(input("Enter a position: "))
    cur_node = head
    i = 0
    while cur_node.next:
        i += 1
        prev_node = cur_node
        cur_node = cur_node.next
        if i == position:
            # delete cur_node
            prev_node.next = cur_node.next
            return


def delete_last_node(head):
    pass


if __name__ == "__main__":
    head = create_singly_linked_list()
    traverse_ll(head)

    print("Delete First node:")
    head = delete_first_node(head)
    traverse_ll(head)

    print("Delete nth node:")
    delete_nth_node(head)
    traverse_ll(head)