#!/usr/bin/python
x = 7
def access_global():
    global x 
    x = 3.5
    print('Value of x from function', x)
access_global() 
print('from global scope x is', x)      
