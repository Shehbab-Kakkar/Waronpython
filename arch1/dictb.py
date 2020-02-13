#!/usr/bin/python
#Filname is dictb.py
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
print('Actual prices\n', prices)

for k, v in prices.items():
    prices[k] = round(v - 0.10, 2)
print('prize after discount\n',prices)
for i, j in prices.items():
    print(i,' prize is = ',j)
