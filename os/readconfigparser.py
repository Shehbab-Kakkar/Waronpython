#!/usr/bin/python
#Filname is readconfigparser.py
from configparser import ConfigParser
p = ConfigParser()
p.read('read_simple.ini')
print(p.get('bug_tracker', 'url'))
