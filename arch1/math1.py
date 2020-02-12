#!/usr/bin/python
#Filname is math1.py
from math import ceil, floor
print(ceil(10.3))
print(floor(10.7))
e = 'Hello'
from math import *
print("value of e = {0} ".format(e))
print(type(e))
import statistics as stats
grades = [85, 93, 45, 87, 93]
print("Grades = ",stats.mean(grades))

import decimal as dec
print(dec.Decimal('2.5') ** 2)
