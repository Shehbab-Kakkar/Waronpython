#!/usr/bin/python
#Filname is getpass.py
import getpass
user_name = getpass.getuser()
print ("User Name : %s" % user_name)
while range(0,3):
            passwd = getpass.getpass("Enter your Password : ")
            if passwd == 'redhat':
                        print ("Welcome!!!")
                        break
            else:
                        print ("The password you entered is incorrect.")
