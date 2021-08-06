class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    """
    -> We can user this magic dunder method to debug an object.
    -> Without this method, if we print object we won't get actual
    object data, we will get an address for that object
    """
    def __repr__(self):
        return "Employee('{}', {})".format(self.name, self.salary)

    def __str__(self):
        return "{} - {}".format(self.name, self.salary)

    def __add__(self, other):
        return self.salary + other.salary

    def __len__(self):
        return len(self.name)


if __name__ == "__main__":
    emp1 = Employee('Omar', 50000)
    emp2 = Employee('Babu', 70000)

    print(emp1.__repr__())
    print(repr(emp1))
    print(emp1)  # So, actually __repr__ is called explicitly

    print(emp1.__str__())
    print(str(emp1))

    print(emp1 + emp2)  # Without __add__ method we couldn't do this

    print(len(emp1))  # Using emp obj to find out len of specific property of emp obj





