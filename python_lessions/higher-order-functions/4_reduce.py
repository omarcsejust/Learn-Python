"""
1. reduce function reduce the iterable object into a single element

2. it takes a function & only one iterable object like filter
"""

from functools import reduce


def add_list_items(x, y):
    return x+y


li = [10, 20, 30, 40, 50]
result = reduce(add_list_items, li)  # reduce with user defined function
print("Reduce with user defined function: ", result)


# reduce with lambda function
result2 = reduce(lambda x, y: x+y, li)
print("Reduce with Lambda: ", result2)


