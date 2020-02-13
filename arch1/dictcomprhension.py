#!/usr/bin/python
#Filname is dictcomprhension.py
incomes = {'apple': 56, 'orange': 35, 'banana': 50}
total = sum([i for i in incomes.values()])
print(total)

incomes = {'a': 56, 'o': 35, 'b': 50}
print(sum(incomes.values()))

incomes = {'apple': 56, 'orange': 35, 'banana': 5}
non_citric = {k: incomes[k] for k in incomes.keys() - {'orange'}}
print(non_citric)
