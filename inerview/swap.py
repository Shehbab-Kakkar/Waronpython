#!/usr/bin/python
#Filname is swap.py
n1 = int(input("n1:"))
n2 = int(input("n2:"))
n2 = n1 + n2
n1 = n2 - n1
n2 = n2 - n1
print(f'n1:{n1}\nn2:{n2}')
