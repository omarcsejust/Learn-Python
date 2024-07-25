# Set Fundamentals
# ----------------
"""
1. Sets are unordered collection like dictionary.
2. Which means the items are we have in the set are not in sequenced
3. That's why we can not access the using index

**List are ordered collection**
"""

# Initialize set
s = set()
print(type(s))

# Or we can initialize like below
st = {2, 5, 5, 'Omar', 10, 12.5, 'Omar'}
print("Set contains all data type & remove duplicate values: ", st)

# Add value to the set
# --------------------
s.add(5)
s.add(10)
s.add(15)
print("Add value in Set: ", s)

# Remove value from Set
# ---------------------
s.remove(10)
print("Remove 10 from set: ", s)

# Length of Set
# -------------
print("Length of Set: ", len(s))

# Get set from a list
num_list = [10, 20, 30, 40, 50, 10, 30, 50]
unique_numbers_from_list = set(num_list)
print("Get a set from List: ", unique_numbers_from_list)

# Union of two sets
# -----------------
"""
Union will return a new set which contains all items
that are either in the first or in the second set
"""
set_one = {10, 20, 30}
set_two = {20, 30, 40, 50}
union_result = set_one | set_two
print("Union result: ", union_result)

# Intersection of two sets
# ------------------------
"""
Intersection will return a new set that will include all items
that are common in both first and second set
"""
intersection_result = set_one & set_two
print("Intersection result: ", intersection_result)

# Difference between two sets
# ---------------------------
"""
In this operation we will get a new set of items
where first set has the additional items that we don't have in second set

e.g: for above two sets, first set has additional number 10, which is not
present in the second set
"""
diff1 = set_one - set_two
diff2 = set_two - set_one
print("Diff between two sets: ", diff2)

# Symmetric Difference
# --------------------
"""
Symmetric Difference is just opposite of intersection: In Symmetric Difference
we will get items that are not common in two sets, the items that are either in
first set or either in second set
"""
symmetric_diff = set_one ^ set_two  # ^ is called carat operator
print("Symmetric Difference: ", symmetric_diff)

# Check existence of an item in a set
# -----------------------------------
if 10 in set_one:
    print("Item 10 found in set_one")

# Loop over set
# -------------
for item in set_two:
    print(item)

