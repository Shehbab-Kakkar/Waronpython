#!/usr/bin/python
#Filname is dictdelseq.py
# File: dict_popitem.py
import time
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
print("dictationary\n", a_dict)
while True:
    try:
        print(f'Dictionary length: {len(a_dict)}')
        item = a_dict.popitem()
        # Do something with item here...
        print(f'{item} removed')
        time.sleep(1)
    except KeyError:
        print('The dictionary has no item now...')
        break
