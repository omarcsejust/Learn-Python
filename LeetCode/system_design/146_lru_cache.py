class Node:
    def __init__(self, key, val, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt


class LRUCache:
    def __init__(self, limit: int):
        self.cache = {}
        self.limit = limit

        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.nxt = self.tail
        self.tail.prev = self.head

    def remove_node(self, node: Node):
        prev = node.prev
        nxt = node.nxt

        prev.nxt = nxt
        nxt.prev = prev

    def add_node(self, node: Node):
        head_next = self.head.nxt

        self.head.nxt = node
        node.prev = self.head

        node.nxt = head_next
        head_next.prev = node

    def put(self, key, val):
        if key in self.cache:
            node = self.cache.get(key)
            self.remove_node(node)

        node = Node(key, val)
        self.cache[key] = node
        self.add_node(node)

        if len(self.cache) > self.limit:
            least_node = self.tail.prev
            self.remove_node(least_node)
            del self.cache[least_node.key]

    def get(self, key: int):
        if key in self.cache:
            node = self.cache.get(key)
            self.remove_node(node)
            self.add_node(node)
            return node.val

        return None

    def visit_linkedlist(self):
        node = self.head.nxt
        print("Cache......")
        while node.nxt:
            print(node.key, " ")
            node = node.nxt


if __name__ == "__main__":
    lru = LRUCache(3)
    lru.put(5, 10)
    lru.put(6, 20)
    lru.put(7, 30)
    lru.visit_linkedlist()

    print(lru.get(6))
    lru.visit_linkedlist()

    lru.put(8, 40)
    lru.visit_linkedlist()




