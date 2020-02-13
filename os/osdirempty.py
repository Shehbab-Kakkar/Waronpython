#!/usr/bin/python
#Filname is osdirempty.py

# Python program to check whether 
# the directory empty or not 
  
  
import os 
  
# path of the directory 
path = "/root/python"
  
# Getting the list of directories 
dir = os.listdir(path) 
print(f"List of files under root directory\n{dir}\n") 
for i in dir:
   print(i) 

# Checking if the list is empty or not 
if len(dir) == 0: 
    print("Empty directory") 
else: 
    print("Not empty directory") 

