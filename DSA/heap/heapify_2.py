heap = [3, 6, 5, 0, 8, 2, 1, 9]
N = len(heap)

def heapify_max(root_i):
    left = 2 * root_i + 1
    right = 2 * root_i + 2

    # find the max value among two childs
    if left < N and right < N:
        swap_i = left if heap[left] >= heap[right] else right
    else:
        swap_i = left # ACBT Tree, i.e: if not both then must have left child

    # recursion termination conditions
    # base condition
    if swap_i >= N:
        return
    
    if heap[root_i] >= heap[swap_i]:
        # already satisfying Max Heap
        return
    
    # child (left/right) > root
    # now perform swapping
    temp = heap[root_i]
    heap[root_i] = heap[swap_i]
    heap[swap_i] = temp
    
    heapify_max(swap_i) # top-down - O(logn)


def heapify(heap):
    for i in range((len(heap) // 2) - 1, -1 , -1):
        heapify_max(i)

if __name__ == '__main__':
    print(heap)
    heapify(heap)
    print(heap)


