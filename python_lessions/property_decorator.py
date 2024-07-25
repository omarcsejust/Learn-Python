"""
1.
https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6
Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters

2.
https://www.youtube.com/watch?v=5-S_B6nAzO8&t=6s
Python Tutorials - Property Decorators Part 1
"""


class Employee:

    def __init__(self, first_name, last_name, salary, age):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.age = age
        self.email__ = "{}.{}@gmail.com".format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, name: str):
        first_name, last_name = name.split(" ")
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first_name, self.last_name)


if __name__ == "__main__":
    emp1 = Employee('Omar', 'Hasan', 50000, 27)
    emp1.first_name = "Rahman"
    print(emp1.email__)  # we have changed first_name property, bt not reflected here

    print(emp1.first_name)
    print(emp1.last_name)

    # decorated property
    print("-------- Getter -------------")
    print(emp1.full_name)
    print(emp1.email)  # we have changed first_name property, and got reflection here

    # setter for decorated property
    print("-------- Setter -------------")
    emp1.full_name = "Fayaz Uddin"

    print(emp1.first_name)
    print(emp1.last_name)
    print(emp1.full_name)
    print(emp1.email)






