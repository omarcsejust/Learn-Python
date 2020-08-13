# list is a mutable data structure in python

# we can store different type of data in a same list
li = [12, 23, 76, 34, 'Omar Hasan']
print(li)


# Add value to a list at the last
li.append(50)
print('Add 50 as new item to list')
print(li)


# A list can have another list in it
li2 = [10, 20, 30]
li.append(li2)
print('Add list to a list')
print(li)


# Get the nested list-->li2 element from main list li
print('Get item of a list')
print(li[6][0])


# change the element of a list
li[4] = 'Babu'
print('Change 5th element as Babu from a list')
print(li)


# Reverse a list
print('Make a list Reverse permanently')
li.reverse()
print(li)


# Slicing list
print("List Slicing [1:5], from index 1 to index 5-1")
print(li[1:5])


print('Reverse a list using Slicing')
print(li[-1::-1])


# pop() method removes the last element from a list
li.pop()  # last element li2 = [10, 20, 30] will be removed from the list li
print('Remove last element from a list')
print(li)


# remove a specific item from a list
del li[1]
print('Remove 2nd element from a list')
print(li)


# delete entire list
del li


# find all numbers those are multiple of 3 or 5
num = list(range(1, 100))  # creating a list of 1 to 99
"""
for i in num:
    if i % 3 == 0 or i % 5 == 0:
        print(i)
"""

# same program with list comprehension
res = [i for i in num if i % 3 == 0 or i % 5 == 0]
print(res)




