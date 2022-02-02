"""
TWO SUM II - Amazon Coding Interview Question - Leetcode 167 - Python
https://www.youtube.com/watch?v=cQ1Oz4ckceM
"""


class TwoSum:

    def __init__(self, numbers, target: int):
        self.numbers = numbers
        self.target = target

    def find_indexes(self, left: int, right: int)->list:
        # recursion termination conditions
        if left == right or len(self.numbers) == 0 or len(self.numbers) == 1:
            return []

        if self.numbers[left] + self.numbers[right] > self.target:
            right -= 1
        elif self.numbers[left] + self.numbers[right] < self.target:
            left += 1
        else:
            return [left, right]

        return self.find_indexes(left, right)


if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 7, 10, 11]
    two_sum = TwoSum(numbers, 9)
    print("Found: ", two_sum.find_indexes(0, len(numbers) - 1))

    numbers2 = [1, 2]
    two_sum2 = TwoSum(numbers2, 3)
    print("Found: ", two_sum2.find_indexes(0, len(numbers2) - 1))

    numbers3 = [1, 2, 4, 5, 8, 12]
    two_sum3 = TwoSum(numbers3, 13)
    print("Found: ", two_sum3.find_indexes(0, len(numbers3) - 1))




