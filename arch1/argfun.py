#!/usr/bin/python
#Filname is argfun.py
x = 8
print("Id of x is ",id(x))
def cube(number):
    print("id of the number", id(number))
    return number ** 3
print(cube(8))
print("##############")
def cube(number):
    print("number is x", number is x)
    return number ** 3
print(cube(70))

print("=============")
def cube(number):
    print(id(number))
    number *= 3
    print(id(number))
    return number
print(cube(7))

