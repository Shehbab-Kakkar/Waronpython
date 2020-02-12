#!/usr/bin/python
#Filname is modified.py
def modified(items):
      for i in range(len(items)):
          items[i] *= 2
      return items
number = [10, 3, 70, 1, 9]
#number = (10, 3, 70, 1, 9) #tuple can't be addeded
print(modified(number))
