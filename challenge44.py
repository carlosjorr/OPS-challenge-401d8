#!/usr/bin/python3

import socket

# Set a timeout value (in seconds)
timeout = 2

# Collect a host IP from the user
hostip = input("Enter the target host IP: ")

# Collect a port number from the user and convert it to an integer data type
portno = int(input("Enter the target port number: "))

def portScanner(hostip, portno):
    sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockmod.settimeout(timeout)
    
    try:
        # Attempt to connect to the target host and port
        sockmod.connect((hostip, portno))
        print("Port open")
    except socket.error:
        print("Port closed")
    finally:
        sockmod.close()

# Call the portScanner function
portScanner(hostip, portno)
