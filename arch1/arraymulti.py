#!/usr/bin/python
#Filname is arraymulti.py
a = [[10,11,12],[21,32,43],[65,76,56]]
for i in a:
   for j in i: 
     print(j,end=' ');
   print()

for index1, i in enumerate(a):
    for index2,j in enumerate(i):
        print(f'a[{index1}][{index2}]={j}', end=' ')
    print() 
  
