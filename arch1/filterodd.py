#!/usr/bin/python
#Filname is filterodd.py
"""
Create the list of odd number from the random number list
"""
random = [10,11,23,34,56,67,89,36]
def searching(random):
     return random%2 == 0
         
var =  list(filter(searching,random)) #  random list is pass to searching function 
print("Old number list: ", var)

print([x for x in random if searching(x)])
"""
it will return true only if x is odd 
"""
    
