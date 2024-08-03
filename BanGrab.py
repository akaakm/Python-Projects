#! /usr/bin/python3

# imports the socket module for interfacing a network connection
import socket

# create a port list of four ports and a for statement that iterates through the list
ports = [21, 22, 25, 3306]

# the for loop takes the ports list and uses each iteration in port for the socket code indented under it
for port in ports:
    s = socket.socket()

    print('This is the banner for the port')
    print(port)

# connect is used with socket to make a network connection to a common localhost IP and each iteration of the port list, the IP can changed to whatever is appropriate
    s.connect(("127.0.0.1", port))

# limits the amount of data read and stores them in the answer variable
    answer = s.recv(1024)

# prints the answer variable data so that we can read it!
    print(answer)

# closes the socket connection
    s.close()

# This script "grabs" the banner information travelling through the input IP address and port list
# Don't forget to use chmod 755 for permission to execute the script if necessary