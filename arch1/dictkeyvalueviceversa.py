#!/usr/bin/python
#Filname is dictkeyvalueviceversa.py
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {value: key for key, value in a_dict.items()}
print(new_dict)
