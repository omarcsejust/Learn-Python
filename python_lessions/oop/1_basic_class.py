"""
=> There are two types of variable in Python
  1. Instance variable
  2. Class/Static variable [we can access class variable by both class object & className]

=> There are three types of method in Python
  1. Instance method
    --> Instance methods deals with instance variables
    --> First parameter must be "self"
    -->

  2. Class method
    --> @classmethod decorator is used to define class methods
    --> We can access class method by both class object & className
    --> First parameter must be "cls"
    --> **We can use class method to create an object of a class
    --> classMethods deals with class variables

  3. Static method
    --> @staticmethod decorator is used to define a static method
    --> We can access Static method by both class object & className
    --> We no need to provide self or cls as a parameter, parameter is totally optional
    --> Static method knows nothing about class state
"""


class Student:
    counter = 0  # this is a class variable

    def __init__(self, name, age, grade):
        # all this are instance variables
        self.name = name
        self.age = age
        self.grade = grade

        #  self.counter += 1  //wrong: to access class variable we must use ClassName
        Student.counter += 1

        # or we can use call method to increment counter class variable (as class method deals with class variable)
        Student.incr_counter()

    def get_grade(self):
        return self.grade

    @classmethod
    def incr_counter(cls):
        cls.counter += 1

    # this is a class method
    @classmethod
    def get_total_students(cls):
        return cls.counter

    # class method works as class object creator
    @classmethod
    def create_class_obj(cls, info_str):
        name, age, grade = info_str.split('-')
        return cls(name, age, grade)


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avg(self):
        total_grade = 0
        for student in self.students:
            total_grade += student.get_grade()

        return total_grade / len(self.students)


if __name__ == "__main__":
    s1 = Student('Omar', 25, 87)
    s2 = Student('Sany', 29, 88)
    s3 = Student('Gazi', 39, 88)

    # class method accessing by both class object & ClassName
    print('Total Students:', Student.get_total_students())  # accessing class method by className
    print('Total Students:', s1.get_total_students())  # accessing class method by class object

    # we can access class variable by both class object & ClassName
    print('Class variable accessing by Obj:', s2.counter)
    print('Class variable accessing by ClassName:', Student.counter)

    # creating class object by class method
    s4 = Student.create_class_obj('Alamin-42-90')
    print('Class object by ClassMethod: Age -', s4.age)

    c = Course('Math', 2)
    c.add_student(s1)
    c.add_student(s2)

    print(c.get_avg())


