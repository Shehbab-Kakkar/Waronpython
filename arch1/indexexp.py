#!/usr/bin/python
#Filname is indexexp.py
list = [67, 12, 46, 43, 13]
key1 = 43
key2 = 44

if key1 in list:
   print(f'{key1} is present at {list.index(key1)}')
else:
   print(f'{key1} not found')
if key2 in list:
   print(f'{key2} is present at {list.index(key2)}')
else:
   print(f'{key2} not found')


