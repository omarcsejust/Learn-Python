# decorator function
def str_upper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner


# decorated function
@str_upper
def print_str():
    return "good morning"


print(print_str())


"""
Decorator function with parameters
"""


# decorator function
def str_upper2(func):
    def inner(st):
        str1 = func(st)
        return str1.upper()
    return inner


# decorated function
@str_upper2
def print_str2(st):
    return st


print(print_str2("hello omar"))


