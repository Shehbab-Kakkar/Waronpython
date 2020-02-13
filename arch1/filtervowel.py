#!/usr/bin/python
#Filname is filtervowel.py
alpa = ['i','j','a','f','u','k','p','o','e','q']

vow = ['a','e','i','o','u']

def comparevowels(alpha):
    if (alpha in vow ):
        return True
    else:
        return False

vowels = filter(comparevowels,alpa) 
"""filter stored in the memory"""
#listing = list(vowels)
#print(listing)
for i in vowels:
    print(i)
