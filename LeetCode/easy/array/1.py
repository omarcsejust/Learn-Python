"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Note:
-----
We can't use two pointer here because the list is not sorted, and we can not sort
the list forcefully because if we do it then we will lost the actual index numbers
"""

from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            for i2 in range(i+1, len(nums)):
                if nums[i] + nums[i2] == target:
                    return [i, i2]


print(Solution.two_sum(Solution(), [2,7,11,15], 9))