#!/usr/bin/python
#Filname is enum1.py
numbers = [2, 5, 4, 7]
print('\nCreate a bar from numbers')
print(f'Index{"Value":>6} Bar')
for index, value in enumerate(numbers):
    print(f'{index:>4}{value:>6} {"@" * value}')
                                 #Seq * integer
