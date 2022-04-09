"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed_brackets = ")]}"
        map_brackets = {')': '(', ']': '[', '}': '{'}

        for bracket in s:
            if stack and bracket in closed_brackets:
                if stack.pop() != map_brackets[bracket]:
                    return False
            else:
                stack.append(bracket)

        if len(stack) == 0:
            return True

        return False


print(Solution.isValid(Solution(), "()[]{}"))