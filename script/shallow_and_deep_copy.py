import copy

old_list = [1, 2, [3, 4], 5, 6]

# This is Shallow Copy or (copy.copy(old_list) is same
new_list = old_list.copy()

new_list.append(7)
new_list[2][0] = 8
new_list[0] = 'AA'

print("Old List: ", old_list)  # Nested list obj [3, 4] has been modified to: [8, 4], bt append(7) not added
print("New List: ", new_list)

# tow list ids are different
print(id(old_list))
print(id(new_list))

'''
But nested list object([3, 4]) ids are same for two list
that's why if we change/update nested list object of old_list or new_list,
the change will be affected in both old_list and new_list list
'''
print(id(old_list[2]))
print(id(new_list[2]))


# Deep Copy
old_li = [1, 2, [3, 4], 5, 6]

new_li = copy.deepcopy(old_li)

new_li.append(7)
new_li[2][0] = 8

print(old_li)
print(new_li)

'''
Now nested list object([3, 4]) ids are different for both old_li and new_li list
Nested list objects are now pointing the different memory locations.
'''
print(id(old_li[2]))
print(id(new_li[2]))

