#!/usr/bin/python
#Filname is argparse1.py
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("blog")
args = parser.parse_args()

if args.blog == 'Work':
    print('You made it!')
else:
    print("Didn't make it!")
