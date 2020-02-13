#!/usr/bin/python
#Filname is zipping.py
name = ['Tom','Hawk','Don']
grade = [3.5,6.5,8.5]
for name, grade in zip(name,grade):
    print(f'Name:{name},Grade:{grade}')
