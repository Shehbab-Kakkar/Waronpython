#!/usr/bin/python
#Filname is oswritevmethod.py
# import os module 
import os 
  
# File path 
path = "/root/python/one/file.txt"
  
# Create a file and get the 
# file descriptor associated  
# with it using os.open() method 
fd = os.open(path, os.O_CREAT | os.O_WRONLY) 
  
  
# Bytes-like objects  
# the data to be written in the file 
buffer1 = bytearray(b"Working hard you will win the game of life ") 
buffer2 = bytearray(b"I will never give up ") 
buffer3 = bytearray(b"doing will till need of life") 
  
# write the data contained in 
# bytes-like objects 
# to the file descriptor fd 
# using os.writev() method 
numBytes = os.writev(fd, [buffer1, buffer2, buffer3]) 
  
# print the content of file 
with open(path) as f: 
    print(f.read()) 
  
# Print the number of bytes actually written 
print("Total Number of bytes actually written:", numBytes) 

