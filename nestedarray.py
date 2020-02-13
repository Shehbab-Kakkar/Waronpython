#!/usr/bin/python
#Filname is nestedarray.py
t = [[10,30,49],[4,6,7]]
total = 0
items = 0
for i in t:
   for item in i:
       total += item
       items += 1
print(total/items)
print("@@@@@@")
total = 0
items = 0
for i in t:
    total += sum(i)
    items += len(i)
print(total)
print(items)     
print(total/items)
