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
            self.name = name
            self.address = address
            self.getStatus()

        except ConnectionRefusedError:
            print("Error al intentar validar conexion.")

    # OBTENER STATUS DEL SERVIDOR
    def getStatus(self):
        message = "status"
        self.sock.sendall(message.encode())
        response = self.sock.recv(256)
        print(response)

    # ENVIAR MENSAJE A TODOS O A DESTINATARIOS
    def sendMessage(self, name, address, origin, message, destination):
        mensage = []
        mensage.append(name)
        mensage.append(address)
        mensage.append(origin)
        mensage.append(destination)
        mensage.append(mensage)
        mensageParse = self.serializar(mensage)
        self.sock.sendall(mensageParse.encode())

    # OBTENER LISTA DE USUARIOS CONECTADOS
    def getListUser(self):
        print("Get list of connected user")

    # CERRAR CONEXION DEL CLIENTE
    def closeConnection(self):
        self.sock.close()

    # SERIALIZAMOS DATOS
    def serializar(self, arrList):
        return ''.join(str(arrList))

    # OBTENER NOMBRE
    def getName(self):
        return self.name

    # OBTENER ADDRESS
    def getAddress(self):
        return self.address
