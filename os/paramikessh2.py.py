#!/usr/bin/python
#Filname is paramikessh2.py.py
import base64
import paramiko

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('server1.example.com', username='shehbab', password='redhat')
stdin, stdout, stderr = client.exec_command('free -m')
for line in stdout:
    print('... ' + line.strip('\n'))
client.close()
