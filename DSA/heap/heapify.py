class Heap:
    def __init__(self, heap):
        self.heap = heap

    def __heapify_internal_nodes_max(self, n: int, i: int):
        left = i * 2 + 1
        right = i * 2 + 2

        # base condition
        # leaf node (no right, no left exists)
        if left >= n and right >= n:
            return

        # either left or right exist
        left_val = self.heap[left] if left < n else float('-inf')
        right_val = self.heap[right] if right < n else float('-inf')

        largest = i
        if left_val > right_val and left_val > self.heap[i]:
            largest = left
        elif right_val >= left_val and right_val > self.heap[i]:
            largest = right

        if largest != i:
            temp = self.heap[i]
            self.heap[i] = self.heap[largest]
            self.heap[largest] = temp
            self.__heapify_internal_nodes_max(n, largest)

    def heapify_max(self):
        n = len(self.heap)
        internal_last_node = (n // 2) - 1
        while internal_last_node >= 0:
            self.__heapify_internal_nodes_max(n, internal_last_node)
            internal_last_node -= 1


if __name__ == "__main__":
    data = [4, 6, 8, 10, 15, 30, 30]
    heap = Heap(data)
    heap.heapify_max()
    print(data)





