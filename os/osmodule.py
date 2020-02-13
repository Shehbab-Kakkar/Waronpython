#!/usr/bin/python
#Filname is osmodule.py
import os
if os.path.isdir("fullone"):
   os.rmdir("fullone")
else:
   print("file note exists")
