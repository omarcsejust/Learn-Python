"""
1. String is immutable(can not modify it) in python

2. String is an object of str class in Python.

3. Python has number of string functions which are in the string library.
These functions are already built into every string

4. These functions do not modify the original string(because string is not mutable),
 instead they return a new string
"""

# String immutable
# ----------------
original_str = "Hello"
print(original_str[1])
# original_str[1] = "o"  # it will through an error

greet = "Hello Omar"
lower_greet = greet.lower()  # returns a new string
print(lower_greet)
print(greet)  # do not modify the original string

# even the const string has builtin methods
# -----------------------------------------
print("Hello There".lower())

print("Upper:", "Hi There".upper())
print("Capitalize: ", "HI THERE".capitalize())

# loop over string
# ----------------

itr_str = "Hello world"
for letter in itr_str:
    print(letter)

print("Also string can be used in index operator: ", itr_str[6])

# searching a string
# ------------------
"""
    b a n a n a
    0 1 2 3 4 5
    
    >> find na string from banana
     i.e: find method returns the position of the first occurrence of given string
"""

banana = "banana"
pos = banana.find("na")
print("Position of na: ", pos)
print("Not found string: ", banana.find("z"))  # return -1 if string not found


# replacing string
# ------------------
"""
str.replace("old string", "new string")
"""

replace_str = "Hello Bob"
print("Replace Str: ", replace_str.replace("Bob", "Ashley"))

# Stripping Whitespace
# --------------------

strip_str = "  Hello Bob      "
print("Remove whitespace from LS: ", strip_str.lstrip(strip_str))
print("Remove whitespace from RS: ", strip_str.rstrip(strip_str))
print("Remove whitespace from Both LS & RS: ", strip_str.strip(strip_str))


