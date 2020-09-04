"""
1. Tuples are immutable

2. Since Python doesn't have to build tuple structures to be modifiable,
that's why tuples are simple and more efficient in term of memory use and
performance than list
"""

tp = (23, 45, 21, 76, 34)
print(tp)
print("2nd Element: ", tp[1])
print("Type is: ", type(tp))

# immutable
# ---------
# tp[1] = 50  # Error

# max element in tuple
# --------------------
print("Max Element in Tuple: ", max(tp))

# min element in tuple
# --------------------
print("Min Element in Tuple: ", min(tp))

# len of tuple
# ------------
print("Length of Tuple: ", len(tp))

# sum of elements in tuple
# ------------------------
print("Sum of Elements in Tuple: ", sum(tp))

# find avg of elements in tuple
# -----------------------------
print("Avg: ", sum(tp)/len(tp))


# Tuple can be used in Assignment Statement
# -----------------------------------------
(x, y) = (10, 20)
print("X: ", x, "Y: ", y)

# (x, y) = (5)  # Error

product, price = "Laptop", 30000.5  # no need parentheses
print("Product: ", product, "Price: ", price)


# Tuple & Dictionaries
# --------------------
"""
The items() method in dictionary returns a list of
(key, value) tuples
"""

di = {
    "name": "Omar",
    "id": "120119",
    "position": "Software Engineer",
    "age": 27
}

list_of_tuples = di.items()
print("List of tuples: ", list_of_tuples)  # e.g: [('name', 'Omar'), ('id', '120119')]

for tp in di.items():
    print("Type of dictionary items: ", type(tp))
    break

for (k, v) in di.items():
    print("Key: ", k, "Value: ", v)
    break

# The above code is just like
for k, v in [('name', 'Omar'), ('id', '120119')]:
    print("Key: ", k, "Value: ", v)
    break


# Sorting List of Tuple by key
# ----------------------------
d = {'a': 10, 'c': 1, 'b': 20}
print(d.items())
print(sorted(d.items()))  # It sorts in key order


# Sort by value instead of key
# ---------------------------
temp = list()
for k, v in d.items():
    temp.append((v, k))  # adding tuple in the list

print("Sort by value: ", sorted(temp))
print("Sort by value reverse: ", sorted(temp, reverse=True))


"""
10.2:
 Write a program to read through the mbox-short.txt and figure out the
 distribution by hour of the day for each of the messages. 
 You can pull the hour out from the 'From ' line by finding the time 
 and then splitting the string a second time using a colon.
e.g: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
 Once you have accumulated the counts for each hour, print out the counts, 
 sorted by hour as shown below.
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

d = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        tmp = line.split()
        tmp_time = tmp[5].split(':')
        d[tmp_time[0]] = d.get(tmp_time[0], 0) + 1

for k, v in sorted(d.items()):
    print(k, v)


