"""
Dictionary are unordered collection
"""

# define dictionary
my_dict = {}  # not set
# or
my_dict = dict()
print(type(my_dict))

dict_person = {
    'name': 'Omar',
    'id': 'AB-1234445',
    'dist': 'Rajshahi',
    'village': 'Bagdhani',
    'age': 27
}

# if key is known the we can get the value by using key
"""
if wrong key is passed, then it will through an  KEY Error:
print(dict_person['named'])  -----> KeyError: 'named'
"""
print(dict_person['name'])

# get() method
# if key is not known we can use get() method to get a value by it's key
# ----------------------------------------------------------------------
"""
it is safe to use get() method to avoid exception.
if key does not exist then it will return None by default instead of terminating the program
"""
print("named key not fount in get(): ", dict_person.get('named'))
print("Default name in get(), if key not found: ", dict_person.get('named', 'Omar Hasan'))

# get all keys from a dictionary
# ------------------------------
dict_keys_list = dict_person.keys()  # return list of dict keys
print("Dict keys list: ", dict_keys_list)

# get all values from a dictionary
# --------------------------------
dict_values_list = dict_person.values()  # return list of dict values
print("Dict values list: ", dict_values_list)

# iteration over dictionary
# -------------------------
# Approach-1:
for key, value in dict_person.items():
    print(key, "=>", value)

# Approach-2:
for key in dict_person.keys():
    print(key, '=>', dict_person[key])

# Add new element to the dictionary or update existing element
# ------------------------------------------------------------
# Approach-01
dict_person['gender'] = 'Male'
print(dict_person)

# Approach-02: using update() method, we can add or update multiple elements at a time
dict_person.update({'name': 'Babu', 'last_name': 'Hasan'})  # update existing name value & add a new element last_name
print(dict_person)

# Copy a dictionary to a new variable
# -----------------------------------
"""
To copay a dictionary to a new variable we should use copy() method.
If we use assignment like dict_new = dict_parent, then the parent dictionary reference will be copied to a new variable
and if we change the parent dictionary the new dictionary will also be changed
"""
dict_person_copy = dict_person
dict_person['new_key'] = 'new key value'
print(dict_person_copy)  # new dictionary also changed

# we should use copy() method to avoid the above problem
dict_person_copy = dict_person.copy()
dict_person['new_key_2'] = 'new key2 value'
print(dict_person_copy)  # new dict not changed

# Check a key exist in a dictionary or not
# ----------------------------------------
# Approach - 01
if 'name' in dict_person:
    print("name key found in person_dict")

# Approach - 02
if 'last_name' in dict_person.keys():
    print("last_name key exist in person_dict")
else:
    print("last_name key not exist in person_dict")

# Reset a dictionary
# ------------------
dict_person.clear()
print(dict_person)




