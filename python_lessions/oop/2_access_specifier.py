"""
**Note: Actually there is no access specifier/modifier in python,
 we can treat properties/method as public, protected, private following some conventions **

1. By default properties are public in python

2. _ (single underscore) before attribute/property and method denotes protected attribute or method
**Note:
-------
 => In C++, C#, Java we can not access protected variable from outside of the class,
 only can use inside the class and in the subclass.
 => But in python we can access protected variable from outside(using obj) of the class
 => We should not practice accessing protected variable outside of the class in python**

3. 2. __ (double underscore) before attribute/property and method denotes private attribute or method
**Note:
-------
 => Normally we can't access private variable from the outside of class
 => We can access private variable from outside of class using "Name Mangling",
 actually python change the private variable name by adding "_ClassName__variableName" before
 the variable.
 => We can assign value to private variable from outside of the class but it will have no effect
"""


class Employee:
    #  __salary = None  [private variable]

    def __init__(self, name, sal, age, roll):
        self.name = name  # public
        self.roll = roll  # public
        self._age = age  # protected
        self.__salary = sal  # private

    # modify private variable
    def set_salary(self, salary):
        self.__salary = salary

    # we can access private variable inside class only
    def get_salary(self):
        return self.__salary

    def display(self):
        print(f'Employee name is {self.name} and Roll is {self.roll} and Salary {self.__salary}')

    def __example_private_method(self):
        print('I am from Private method')


e1 = Employee('Rahul', 50000, 32, 'Software Engineer')
e2 = Employee('Sabbir', 90000, 40, 'CTO')

e1.display()

# working with private variable and methods
# -----------------------------------------
#  print(e1.__salary) (attribute error)[we can not access salary attribute like this way]
print(e1._Employee__salary)  # Name mangling [we should not access private variable from outside of class, like this way also]

# trying to modify private variable directly accessing by object
e1.__salary = 30000  # salary will not be updated, it will remains 50000
print(e1._Employee__salary)

# update private variable using setter method
e1.set_salary(30000)
print(e1._Employee__salary)

# access private method
e1.__example_private_method()

