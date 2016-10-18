# Script Name	: Telnet.py
# Author		: William Berriel
# Created		: November 23 2015  
# Last Modified	: 
# Version		: 0.01

# Modifications	: 

# Description	: This class handles telnet upkeep. It will eventually handle errors.

import sys
import telnetlib

class Homeworks_Telnet_Connection(object):
    'A class that holds the telnet connection, handles setup & teardown, and any metadata.'
    def __init__(self, hostname, username, password, port = 23):
       self.hostname = hostname
       self.username = username
       self.password = password
       self.port = port
       
    def connect(self):
        self.connection = telnetlib.Telnet(self.hostname, self.port)
        self.connection.read_until('login:')
        self.connection.write(self.username + ',' + self.password + "\n")
    
    def disconnect(self):
        if self.connection.get_socket != 0:
            self.connection.close()
    
    def sendLn(self, line):
        if self.connection.get_socket != 0:
            self.connection.write(line)
    
    def readLn(self):
        if self.connection.get_socket != 0:
            self.connection.read_until("\n")
            
        
    
       