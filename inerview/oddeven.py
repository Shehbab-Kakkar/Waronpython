#!/usr/bin/python
#Filname is oddeven.py
while 1:
  num =  int(input("Enter number and check if it is odd and even: "))
  if num != -1:
      if num%2 == 0:
       print(f'{num} is even')
      else:
       print(f'{num} is odd')
  elif num == -1:
      print(f'number is {num} therefore exiting')
      exit()
  else:
    print('No condition')
