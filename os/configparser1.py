#!/usr/bin/python
#Filname is configparser1.py
import configparser
config = configparser.ConfigParser(allow_no_value=True)
config['DEFAULT'] = {
    'title':'book',
    'compression':'yes',
    'compression_level':'20'
}
config.add_section('webserver')
config.set('webserver','server1.example.com')
config.set('webserver','server2.example.com')
config.set('webserver','server3.example.com')

config['database'] = {}
database = config['database']
database['Hostname'] = 'localhost'
database['Username'] = 'username'
database['Password'] = 'password'
database['Keepalive'] = 'no'

with open('configuration.ini','w') as configfile:
     config.write(configfile)
