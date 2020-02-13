#!/usr/bin/python
#Filname is dict.py
states = {'VI': 'Velmin', 'NY': 'Newyork'}
#len(states)
#print(states)
for key in states:
    print(states[key])

for key in states:
    print(key,' = ',states[key])
print("===========")
tv = states.items()# it wil convert them into tuples

for i in tv:
    print(i)
    print(type(i))
num = {'A' : 'aa', 'B' : 'bb', 'C' : 23}
for i, j in num.items():
    print(i,' <--> ',j)
    print(type(i),type(j))
