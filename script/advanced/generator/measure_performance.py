import random
import time

names = ['Omar', 'Babu', 'Nabab', 'Joty', 'Shameem']
subject = ['Chemistry', 'Biology', 'Mathematics']


def student_list(n):
    std_li = []
    for i in range(n):
        student = {
            'id': i,
            'name': random.choice(names),
            'subject': random.choice(subject)
        }
        std_li.append(student)
    return std_li


def student_generator(n):
    for i in range(n):
        student = {
            'id': i,
            'name': random.choice(names),
            'subject': random.choice(subject)
        }
        yield student


star_time_li = time.clock()
students_li = student_list(1000000)  # generating 1M student using List Data Structure
end_time_li = time.clock()

star_time_gen = time.clock()
student_gen = student_generator(1000000)  # generating 1M students using Generator Concept
end_time_gen = time.clock()


print("Time taken bu List: ", end_time_li - star_time_li)
print("Time taken by Generator: ", end_time_gen - star_time_gen)


