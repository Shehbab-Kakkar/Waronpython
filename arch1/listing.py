#!/usr/bin/python
#Filname is listing.py
c = [45, 6, 67, 78, 30, 97]
print(c[-1])
print(len(c))
c[5] = 45
a_list = []
for index in range(1, 6):
    a_list = a_list + [index]
print(a_list)
print("===============\n")

for i in range(len(c)):
   # print('{}: {}'.format(i, c[i]))
    print(f'{i}: {c[i]}')
