x = 50
y = 90
l = [10]


def add():
    # Error: x is not referenced
    '''
    we are adding 10 with x(i.e: x+10), bt x not initialised in this func
    '''
    #x = x + 10

    # update global value of x to everywhere
    global x
    x = x + 10
    print("Inside Func, Global X: ", x)

    # to keep x as its global value original to outside of this func
    y = globals()['y']
    y = y + 10
    print("Inside Func, Global Y: ", y)

    l.append(20)


add()
print("Outside Func, Global X: ", x)
print("Outside Func, Global Y: ", y)
print(l)


