x = 10


def outer():
    y = 20  # y is neither global nor local variable, it's called nonlocal variable

    def inner():
        z = 30
        nonlocal y  # To modify y we need to use nonlocal keyword (y is nonlocal in inner func)
        y = y + 1
        print("Inner func local variable Z : ", z)
        print("Outer function local variable modified inside inner func Y: ", y)

    print("Outer function local variable before modified inside inner func Y: ", y)
    inner()


outer()

