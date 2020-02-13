#!/usr/bin/python
#Filname is ospathstatus.py
import os 
path = '/root/python/one'
# Get the status of 
# the specified path 
status = os.stat(path) 
# Print the status 
# of the specified path 
print(status.st_size) 

