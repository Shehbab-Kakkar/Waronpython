#!/usr/bin/python
#Filname is lambdatemp.py
c = int(input('Enter celious number: '))
d = lambda c: 9/5*c + 32
print(d(c))

print("=========")
number = [10,20,30]
val = list(map(lambda x: ((x - 32)*5/9), number))
print(val)
print("=========")

v1 = int(input("Enter the values:"))
list = []
for i in range(v1):
   list.append(int(input("")))
   
print(list)
