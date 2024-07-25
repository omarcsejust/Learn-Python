def heapify(i):
    if i == 0:
        return
    
    # find the root of newly added i'th child(left/right)
    if i % 2 == 0:
        # i is the RIGHT child of root_i
        root_i = (i - 2) // 2
    else:
        # i is the LEFT child of root_i
        root_i = (i - 1) // 2

    # now check newly added node (child-i) is smaller than it's root or not to satisfy max heap
    if max_heap[root_i] >= max_heap[i]:
        # already satisfying Max Heap
        return
    
    # child (left/right) > root
    # now perform swapping
    temp = max_heap[root_i]
    max_heap[root_i] = max_heap[i]
    max_heap[i] = temp

    # now consider the root_i as child and check child(root_i) < parent of root_i
    heapify(root_i) # bottom-up - O(logn)


heap = [3, 6, 5, 0, 8, 2, 1, 9]
max_heap = []
for i, n in enumerate(heap):
    max_heap.append(n)
    heapify(i)

print(max_heap)

