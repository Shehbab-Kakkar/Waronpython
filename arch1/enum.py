#!/usr/bin/python
#Filname is enum.py
l1 = [10, 20, 40]
s1 = "Hello"
#print(type(l1))
#print(type(s1))
el1 = enumerate(l1)
sl1 = enumerate(s1)
#print(list(el1))
print((el1))
print("############")
for index, number in el1:
    print(f'{index}:{number}')
print( list(sl1))
