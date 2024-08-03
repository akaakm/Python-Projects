#! /usr/bin/python3

# declare python and import socket for the script
import socket

# define the variables to hold the TCP/IP address, port, buffer size of the connection
TCP_IP = "1.1.1.1"
TCP_PORT = 1111
BUFFER_SIZE = 100

# define the socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# add IP and port variables to socket and tell socket to use the listen method from the socket library
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

# IP and port of the connection are read using sockets accept method and prints the information
conn, addr = s.accept()
print('Connection address: ', addr)

# adds a break condition to keep the script running until it receives information
while True:

        data=conn.recv(BUFFER_SIZE)
        if not data:
                break
        print("Received data: ", data)
        conn.send(data) #echo

conn.close()

# this script is a TCP Listener for any connections to your system or server. make sure you enter the correct tcp ip and tcp port for the server or system you want monitored