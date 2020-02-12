#!/usr/bin/python
#Filname is seq.py
number = [20, 30, 40, 50]
#number.index(100)
key = 300
if key in number:
    print(f'{key} found at index {number.index(key)}')
else:
    print(f'{key} not found')
