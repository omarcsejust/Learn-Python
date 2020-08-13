# Required argument & Optional argument
def req_arg(m, n=5):
    print("Required arg:", m)
    print("Optional arg:", n)


# Arg serial does not matter
def arg_serial(m, n):
    print("This is arg m: ", m)
    print("This is arg n: ", n)


# Non-key worded arg
"""
If we don't know how much of arg we need to pass
then we can use non-key worded arg like below.
The arg will act as a tuple
In JS it is called Rest Parameter (...m)
"""


def non_key_worded_arg(*tp):
    print(type(tp))  # tp is a tuple
    for i in tp:
        print(i)


# Key-worded arg
def key_worded_arg(**d):
    print(type(d))  # d is a dictionary
    for key, value in d.items():
        print(key, '=>', value)


if __name__ == "__main__":
    # if we don't pass n then it does not matter, but you have to pass required arg m
    # req_arg(10)

    # Arg serial does not matter
    # arg_serial(n=10, m=20)

    # Non-key warded arg
    non_key_worded_arg(10, 20, 30, 40, 50)

    # key-worded agr
    key_worded_arg(name='Omar', age=27, address='Rajshahi')

