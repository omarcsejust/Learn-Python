nums = [3, 2, 1]
res = []
def subsets(i: int, subset: list):
    if i == len(nums):
        res.append(subset[:])
        return
    subset.append(nums[i])
    
    subsets(i + 1, subset)
    subset.pop()
    subsets(i+1, subset)

subsets(0, [])
print(res)


