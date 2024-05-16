class Node:
    def __init__(self) -> None:
        self.val = None
        self.left = None
        self.right = None


def build_tree():
    val = int(input("Enter a value: "))
    if val < 0:
        return
    
    node = Node()
    node.val = val
    print(f"Left of {val}")
    node.left = build_tree()

    print(f"Right of {val}")
    node.right = build_tree()

    return node

def dfs_postorder(root):
    if root is None:
        return
    
    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.val, " ")

root = build_tree()
dfs_postorder(root)