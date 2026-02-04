nums = [3, 2, 1]
res = []
def subset_sums(indx: int, sm, target: int, subset: list):
    if indx == len(nums):
        if sm == target:
            print(subset, sm)
            res.append(subset.copy())
        return
    
    subset.append(nums[indx])
    sm += nums[indx]
    subset_sums(indx + 1, sm, target, subset)
    subset.pop()
    sm -= nums[indx]
    subset_sums(indx + 1, sm, target, subset)

target = 3
subset_sums(0, 0, target, [])
print(res)

