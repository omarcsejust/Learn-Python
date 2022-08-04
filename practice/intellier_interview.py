# Question-01: What will be the output?
li = ['a', 'b', 'c', 'd', 'e']
print(li[10:])


# Question-02: What will be the output?
def func():
    return [lambda x: x * i for i in range(4)]


li = [m(2) for m in func()]
print(li)


# Question-03: What will be the output?
class Parent(object):
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print(Parent.x, Child1.x, Child2.x)

Parent.x = 2
print(Parent.x, Child1.x, Child2.x)

Child2.x = 3
print(Parent.x, Child1.x, Child2.x)

