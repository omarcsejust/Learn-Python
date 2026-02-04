nums = [3, 2, 1]

def subset_sum(indx: int, sm, target: int, subset: list) -> bool:
    if indx == len(nums):
        print(subset, sm)
        if sm == target:
            # print(subset)
            return True
        return False
    
    subset.append(nums[indx])
    sm += nums[indx]
    if subset_sum(indx + 1, sm, target, subset):
        return True
    subset.pop()
    sm -= nums[indx]
    if subset_sum(indx + 1, sm, target, subset):
        return True
    return False

target = 10
res = subset_sum(0, 0, target, [])
print(res)

