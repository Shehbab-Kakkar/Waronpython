#!/usr/bin/python
#Filname is two.py
from one import onefun
def second():
     x = 'I am from second calling first in second line'
     onefun()
     return x
print(second()) 
