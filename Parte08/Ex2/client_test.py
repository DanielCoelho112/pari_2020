#!/usr/bin/env python
# --------------------------------------------------

# Adapted from https://stackabuse.com/basic-socket-programming-in-python/
# -------------------------------------------------
import socket
import time
import dog_lib

dog = dog_lib.Dog(name='Bob', age=1, color='black')  # instantiate a new dog
dog.addBrother('Lass')
dog.addBrother('Toby')
print('CLIENT: my dog has ' + str(dog))






sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create TCP/IP socket
local_hostname = socket.gethostname()  # retrieve local hostname
local_fqdn = socket.getfqdn()  # get fully qualified hostname
ip_address = socket.gethostbyname(local_hostname)  # get the according IP address

server_address = (ip_address, 23456)  # bind the socket to the port 23456, and connect
sock.connect(server_address)
print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

# define example data to be sent to the server
messages = [dog.name,dog.age,dog.color]
for message in messages:
    print ('Sending message: ' + str(message))
    message_formated = str(message).encode("utf-8")
    sock.sendall(message_formated)
    time.sleep(2)  # wait for two seconds

for message in dog.brothers:
    print ('Sending message: ' + str(message))
    message_formated = str(message).encode("utf-8")
    sock.sendall(message_formated)
    time.sleep(2)  # wait for two seconds



sock.close()  # close connection
