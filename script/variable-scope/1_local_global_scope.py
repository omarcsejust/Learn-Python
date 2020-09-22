"""
L = Local
E = Enclosed
G = Global
B = Built-In
"""


# Local scope
def func_local_scope():
    local_var = 10
    print("Local Variable: ", local_var)


# The scope of local_var is only inside the func_local_scope() function
# print(local_var)  # Error


# Global Scope
x = 100


def func_global_scope():
    global x  # To modify the global variable inside the local scope, we need to use global keyword
    x = x + 1


print("Global Variable before update: ", x)
func_global_scope()
print("Global Variable after update: ", x)

