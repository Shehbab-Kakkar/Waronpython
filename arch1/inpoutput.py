#!/usr/bin/python
#Filname is inpoutput.py
#var1 = input('Enter the value: ')
#print(var1)
var2 = 	open('File.txt','w+')
print(var2)
print(var2.name)
var2.write("Hello my name is bob\n")
var2.write("Second line is ok\n")
var2.write("Third fine hai ji\n")
var2.close()
var2 =  open('File.txt','r')
for i in var2:
  print(i.readline(2))
var2.close()
