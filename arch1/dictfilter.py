#!/usr/bin/python
#Filname is dictfilter.py
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {}
for k, v in a_dict.items():
    if v <= 3:  #compare value
       new_dict[k] = v # Assign value
       print(new_dict[k])
print(new_dict)
print("##########")
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {y:x for x, y in a_dict.items() if y <= 2 }
print(new_dict)
