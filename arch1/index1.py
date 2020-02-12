#!/usr/bin/python
#Filname is index1.py
number = [3, 7, 1, 4, 2, 8, 5, 6]
print(number.index(5))
number *= 2 # number = number * 2
print(number)
print(number.index(5,7)) 
#start counting index position 
#of 5 start from the 7 means second 5

print(number.index(7,0, 4)) #index of 7 inbetween 0 and 4 position

