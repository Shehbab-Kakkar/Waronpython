#!/usr/bin/python
#Filname is dictsorted.py
mydict = {
    "carl": 40,
    "alan": 2,
    "bob": 1,
    "danny": 3,
}

for key in sorted(mydict.keys()):
    print("%s: %s" % (key, mydict[key]))

