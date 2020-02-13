#!/usr/bin/python
#Filname is genexp.py
number = [10, 30, 56, 7, 11]
for i in (x ** 2 for x in number if x%2 !=0):
    print(f"{i}",end="~")
print("\n")

"""gen exp not create a list infact it stores an object 
in memory"""

object_in_memory = (x **2 for x in number if x%2 !=0)
print(object_in_memory)
