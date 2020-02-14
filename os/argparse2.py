#!/usr/bin/python
#Filname is argparse2.py

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('blog', nargs='?', default="JournalDev")
args = parser.parse_args()

if args.blog == 'JournalDev':
    print('You made it!')
else:
    print("Didn't make it!")
