#!/usr/bin/python
#Filname is ospathsyslink.py
# Python program to explain os.path.isdir() method 
# importing os.path module 
import os.path 
dirname = "newdirectory"
# Create a directory 
# (in current working directory) 
if dirname != "newdirectory":
   os.mkdir(dirname) 
# Create a symbolic link 
# pointing to above directory 
symlink_path = "/root/python/one_link"
os.symlink(dirname, symlink_path) 
path = dirname 
# Now, Check whether the 
# specified path is an 
# existing directory or not 
isdir = os.path.isdir(path) 
print(isdir) 
path = symlink_path 
# Check whether the 
# specified path (which is a 
# symbolic link ) is an 
# existing directory or not 
isdir = os.path.isdir(path) 
print(isdir) 

