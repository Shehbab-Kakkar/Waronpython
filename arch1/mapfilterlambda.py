#!/usr/bin/python
#Filname is mapfilterlambda.py
number = [10,3,4,5,7,8,6,71,45]
print(number)
print(list(map(lambda x : x ** 2, filter(lambda x: x%2 != 0, number))))

print("======================")
number = (10,3,4,5,7,8,6,71,45)
print([x ** 2 for x in number if x%2 !=0 ])
