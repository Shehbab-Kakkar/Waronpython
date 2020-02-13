#!/usr/bin/python
#Filname is genexprtext.py
numlist = [10, 3, 7, 1, 9, 4, 2] 
print( list((x ** 2 for x in numlist if x%2 == 0)))

