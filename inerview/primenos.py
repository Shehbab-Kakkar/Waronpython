#!/usr/bin/python
#Filname is primenos.py
num = int(input('Enter the number: '))
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not FIRST a prime number")
           print(i)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not SECOND a prime number")
