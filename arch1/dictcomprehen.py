#!/usr/bin/python
#Filname is dictcomprehen.py
color = ['Green','Yellow','Black','White']
objects = ['color','animals','birds','mind']
dict_new = zip(objects,color)
print(dict_new)
for k,v in dict_new:
    print(f'{k}   - {v}')

color = ['Green','Yellow','Black','White']
objects = ['color','animals','birds','mind']
dict_new = zip(objects,color)
print({x:y for x,y in dict_new})

