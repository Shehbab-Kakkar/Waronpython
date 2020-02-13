#!/usr/bin/python
#Filname is temp.py
# function definition to convert from c to F
def ctof(c):
    f=9/5*c+32
    return f


# input 
c=int(input("Enter Temp(C): "))
# function call
f=ctof(c)
# print 
print("Temp(F) :",f)

