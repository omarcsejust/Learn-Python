nums = [3, 2, 1]

def subset_sum_count(indx: int, sm, target: int, subset: list) -> int:
    if indx == len(nums):
        if sm == target:
            return 1
        return 0
    
    subset.append(nums[indx])
    sm += nums[indx]
    count_left = subset_sum_count(indx + 1, sm, target, subset)
    subset.pop()
    sm -= nums[indx]
    count_right = subset_sum_count(indx + 1, sm, target, subset)
    return count_left + count_right


target = 10
res = subset_sum_count(0, 0, target, [])
print(res)