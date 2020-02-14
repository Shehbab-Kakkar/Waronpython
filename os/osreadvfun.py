#!/usr/bin/python
#Filname is osreadvfun.py
import os 
path = "./file.txt"
fd = os.open(path, os.O_RDONLY) 
size = 20 
buffer1 = bytearray(size) 
buffer2 = bytearray(size) 
buffer3 = bytearray(size) 
numBytes = os.readv(fd, [buffer1, buffer2, buffer3]) 
print("Data read in buffer 1:", buffer1.decode()) 
print("Data read in buffer 2:", buffer2.decode()) 
print("Data read in buffer 3:", buffer3.decode()) 
print("\nTotal Number of bytes actually read:", numBytes) 

