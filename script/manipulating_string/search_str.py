"""
str = From stephen.marquard@utc.ac.za Sat Jan 509:14:16 2020
find the string (utc.ac.za) from the above string
"""
text = "From stephen.marquard@utc.ac.za Sat Jan 509:14:16 2020"
start_pos = text.find("@")

# now find the whitespace pos from the start_pos
end_pos = text.find(" ", start_pos)

# now use slicing to find the desired string
desired_string = text[start_pos+1:end_pos]

print(desired_string)

