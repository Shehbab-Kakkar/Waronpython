#!/usr/bin/python
import paramiko
import argparse
import getpass
parser = argparse.ArgumentParser()
parser.add_argument('-H','--hostname',dest='host', required=True, help="hostname")
parser.add_argument('-u','--username',dest='user', required=True, help="username")
parser.add_argument('-p','--password',dest='passwd',nargs='?', help="password")
parser.add_argument('-c','--command',dest='cmd', required=False, help="command")
args = parser.parse_args()

hostname = args.host 
username = args.user
command = args.cmd
if args.passwd is None:
  password = getpass.getpass('Enter password: ')
else:
  password = args.passwd  
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
