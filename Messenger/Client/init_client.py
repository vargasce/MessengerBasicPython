# -*- coding: utf-8 -*-

import socket

class socketClient():

    def __init__(self, name, address, formView):
        try:

            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_address = ('localhost', 19813)
            self.sock.connect(self.server_address)
            self.rum = True
            self.formV = formView
            self.getStatus()

        except ConnectionRefusedError:
            print("Error al intentar validar conexion.")

    def getStatus(self):

        message = "status"
        self.sock.sendall(message.encode())
        response = self.sock.recv(256)
        print(response)

    def sendMessage(self, origin, destination, message):
        print(origin, destination, message)

    def getListUser(self):
        print("Get list of connected user")

    def closeConnection(self):
        self.sock.close()

# print('Create conection server')
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# print('Connect the socket ti the port whre the server is listening')
# server_address = ('localhost', 19813)

# print('connecting to {} port {}'.format(*server_address))
# sock.connect(server_address)

# try:

    # _End = False

    # while _End == False:

        # message = input('Inser Command : ')
        # print(message)
        # if message == "exit":
            # _End = True
        # else:
            # print('sending {!r}'.format(message))
            # sock.sendall(message.encode())
            # amount_received = 0
            # amount_expected = len(message)
            # data = sock.recv(256)
            # amount_received += len(data)
            # print('received {!r}'.format(data.decode()))
            # if data:
                # data = data
            # else:
                # print('Salgo por break')

# except ValueError:
    # print(ValueError)
    # sock.close()
# finally:
    # print('closing socket')
    # # sock.close()
