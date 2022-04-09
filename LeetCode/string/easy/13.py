"""
13. Roman to Integer
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        sum = 0
        p = 0
        while p < len(s):
            if p+1 <= len(s)-1 and roman_to_int[s[p]] < roman_to_int[s[p+1]]:
                sub = roman_to_int[s[p + 1]] - roman_to_int[s[p]]
                sum += sub
                p += 2
            else:
                sum += roman_to_int[s[p]]
                p += 1

        return sum


print(Solution.romanToInt(Solution(), "LVIII"))
print(Solution.romanToInt(Solution(), "MCMXCIV"))

