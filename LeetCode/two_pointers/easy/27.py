"""
27. Remove Element
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 0
        while r < len(nums):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
                r += 1
            else:
                r += 1

        return l


li = [3,2,2,3]
print(Solution().removeElement(li, 3))
print(li)
print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))


