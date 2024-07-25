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


