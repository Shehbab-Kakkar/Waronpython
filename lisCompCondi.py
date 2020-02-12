#!/usr/bin/python
#Filname is lisCompCondi.py
"""Even number with list comprehension"""
list = [item for item in range(1, 6) if item%2 == 0]
print(list)

"""Upper case letters"""
list2 = ['fhtyhj','htjt','fdf']
list2 = [ item.upper() for item in list2 ] 
print(list2)

"""Tuples with the cubes"""
list3 = [(item, item ** 3) for item in range(1, 6)]
print(list3)

"""List of mutliple of 3 from 3 to 30"""
list4 = [item  for item in range (3, 30, 3)]
print(list4)
