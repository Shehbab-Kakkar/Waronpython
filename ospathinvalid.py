#!/usr/bin/python
#Filname is ospathinvalid.py
# Python program to check whether 
# the directory is empty or not 
import os 
# Function to Check if the path specified 
# specified is a valid directory 
def isEmpty(path): 
	if os.path.exists(path) and not os.path.isfile(path): 
		# Checking if the directory is empty or not 
		if not os.listdir(path): 
			print("Empty directory") 
		else: 
			print("Not empty directory") 
	else: 
		print("The path is either for a file or not valid") 


# path to a file 
path = "/root/python/one"

isEmpty(path) 
print() 

# valid path 
path = "/root/python"
isEmpty(path) 

