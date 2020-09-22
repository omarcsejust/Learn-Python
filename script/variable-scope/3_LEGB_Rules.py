"""
LEGB Rules:
Local --> Enclosed --> Global --> Built-In

Priority: low --> high

Note:
-----
Python first search a variable inside local scope if not found then it searches in
Enclosed scope, if not found it searches in Global Scope, then it searches for Built-In
Variable
"""

x = 10  # Global


# Local scope
def outer():
    x = 20  # Enclosed

    def inner():
        x = 30  # Local
        print("Local X : ", x)

    inner()


outer()


# Enclosed scope
def outer_2():
    x = 20

    def inner_2():
        # x = 30
        print("Enclosed X : ", x)

    inner_2()


outer_2()


# Global scope
def outer_3():
    # x = 20

    def inner_3():
        # x = 30
        print("Global X : ", x)

    inner_3()


outer_3()
