#!/usr/bin/python
#Filname is dictsort.py
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
sort_i = {k: incomes[k] for k in sorted(incomes)}
print(sort_i)

incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
#sort_i = {(k,'->',incomes[k]) for k in sorted(incomes)}
for k in sorted(incomes):
    print(k,'->',incomes[k])
#print(sort_i)


