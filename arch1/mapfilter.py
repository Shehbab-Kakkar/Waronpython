#!/usr/bin/python
#Filname is mapfilter.py
def myfunc(n):
  return lambda a : a - n
 #               11 : 11 - (-2)
mydoubler = myfunc(-2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
def double(x):
   return x * 2
print(double(2))
double1 = lambda y: y * 2
print(double1(5))

print(list(map(lambda var: var%2 != 0, range(0,10))))
print(list(filter(lambda var: var%2 == 0, range(0,10))))
#!/usr/bin/python
#Filname is mapfilter.py

