#!/usr/bin/python
#Filname is paramikessh.py
import sys, paramiko
import getpass

if len(sys.argv) <= 3:
    print ("args missing")
    sys.exit(1)

hostname = sys.argv[1]
password = getpass.getpass('Enter password: ')
command = sys.argv[3]
username = sys.argv[2]
port = 22

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.connect(hostname, port=port, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(command)
    for line in stdout:
	    print('... ' + line.strip('\n'))

finally:
    client.close()
