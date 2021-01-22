#!/usr/bin/env python
import socket
import dog_lib

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create TCP/IP socket
local_hostname = socket.gethostname()  # retrieve local hostname (127.0.0.1)
local_fqdn = socket.getfqdn()  # get fully qualified hostname
ip_address = socket.gethostbyname(local_hostname)  # get the according IP address

# output hostname, domain name and IP address
print ("working on %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))
server_address = (ip_address, 23456)  # bind the socket to the port 23456

print ('starting up on %s port %s' % server_address)
sock.bind(server_address)

# listen for incoming connections (server mode) with one connection at a time
sock.listen(1)


while True:
    print ('waiting for a connection')

    try:
        # print('SERVER: my dog has ' + str(dog))
        print('SERVER: my dog has ' + str(dog))
    except:
        pass

    connection, client_address = sock.accept()  # wait for a connection


    try:  # show who connected to us
        print ('connection from', client_address)
        i = 0
        Dog_name = ''
        Dog_age = ''
        Dog_color = ''
        Dog_brother = []


        while True:  # receive the data in small chunks (64 bytes) and print it
            data = connection.recv(64)
            if data:
                i += 1
                # print(type(data))
                print ("Data: %s" % data)  # output received data

                if i == 1:
                    Dog_name = data
                if i == 2:
                    Dog_age = data
                if i == 3:
                    Dog_color = data
                if i > 3:
                    Dog_brother.append(data)

            else:
                print ("no more data.")  # no more data -- quit the loop
                dog = dog_lib.Dog(name=Dog_name, age=Dog_age, color=Dog_color)  # instantiate a new dog
                for brother in Dog_brother:
                    dog.addBrother(brother)

                break
    finally:
        # Clean up the connection
        connection.close()
