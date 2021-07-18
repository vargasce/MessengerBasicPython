# -*- coding: utf-8 -*-

import socket
import dispacher as dpc

client = {}
public_client = {}
num_connection = 0

print("Creating a TCP/IP Socket")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Bind socket to the port')
server_address = ('localhost', 19813)

print('starting up on {} port {}'.format(*server_address))

sock.bind(server_address)

print('Listen for incoming connection')
sock.listen(1)

while True:
    try:
        num_connection += 1
        connection, cliente_address = sock.accept()
        client['con_'+str(num_connection)] = connection
        public_client['con_'+str(num_connection)] = cliente_address

        try:
            print("Connection from", cliente_address)
            disp = dpc.Dispacher(connection, cliente_address, 'con_'+str(num_connection), num_connection, client,
                                 public_client)
            disp.start()
        except ValueError:
            print(ValueError)
        finally:
            print("Finally init_server.")
    except ValueError:
        connection.close()
        print(ValueError)
