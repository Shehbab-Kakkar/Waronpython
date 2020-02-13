#!/usr/bin/python
#Filname is lambdafilter.py
number = [10,11,21,44,51,78]
#def oddcheck(x):
#    return x%2 != 0
#print(list(filter(oddcheck, number)))
print(list(filter(lambda x: (x%2 == 0), number)))
print(list(map(lambda x: (x%2 == 0), number)))
