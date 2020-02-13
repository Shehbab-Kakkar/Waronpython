#!/usr/bin/python
#Filname is createfilew.py
fh = open("hello.txt","w") 
lines_of_text = ["One line of text here\n", "and another line here\n", "and yet another here\n", "and so on and so forth\n"] 
fh.writelines(lines_of_text) 
fh.close() 
