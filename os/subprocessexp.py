#!/usr/bin/python
#Filname is subprocessexp.py
import subprocess
#Good view of shell commmands as it is

subprocess.call('ls -l | grep -i py',shell=True)

#Ugly view of shell commands in a single line.

print(subprocess.check_output('ls -l | grep -i py',shell=True))


#subprocess.call('python3.6 ../ping.py "Check it out this man"',shell=True)
#######################
#
subprocess.call('yum install tree -y',shell=True)
