#!/usr/bin/python
#Filname is paramikessh3.py
import paramiko
import time
import sys
if len(sys.argv) <= 4:
    print("args missing")
    sys.exit(1)

hostname = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
command = sys.argv[4]
port = 22
ssh = paramiko.SSHClient() #SSHClient() is the paramiko object</n>
#Below lines adds the server key automatically to know_hosts file.use anyone one of the below
ssh.load_system_host_keys() 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
#Here we are actually connecting to the server.
  ssh.connect(hostname, port=port, username=username, password=password)
  time.sleep(5)
#I have mentioned time because some servers or endpoint prints there own information after 
#loggin in e.g. the version, model and uptime information, so its better to give some time 
#before executing the command.
#Here we execute the command, stdin for input, stdout for output, stderr for error
  stdin, stdout, stderr = ssh.exec_command(command)
#Here we are reading the lines from output.
  output = stdout.readlines() 
  print(output)
#Below all are the Exception handled by paramiko while ssh. Refer to paramiko.org for more information about exception.
except (BadHostKeyException, AuthenticationException,  
    SSHException, socket.error) as e:           
    print(e)
