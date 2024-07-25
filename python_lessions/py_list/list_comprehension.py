# find all numbers those are multiple of 3 or 5
num = list(range(1, 100))  # creating a list of 1 to 99
"""
for i in num:
    if i % 3 == 0 or i % 5 == 0:
        print(i)
"""

# same program with list comprehension
res = [i for i in num if i % 3 == 0 or i % 5 == 0]
print(res)

