"""
26. Remove Duplicates from Sorted Array
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        size = len(nums)
        while r < size:
            if r+1 < size and nums[r] != nums[r+1]:
                nums[l] = nums[r]
                l += 1
                r += 1
            elif r+1 >= size:
                # last element, which is always unique at nums[l]
                nums[l] = nums[r]
                r += 1
            else:
                r += 1

        return l + 1


li = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(Solution().removeDuplicates(li))
print(li)
