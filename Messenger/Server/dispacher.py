#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 02:15:53 2021
@author: cristiano
"""
import threading
import sys
import json
from Serializable.serialice import Serialice as srce
from Models.conectionListModel import ListConnection

class Dispacher (threading.Thread):

    def __init__(self, conection, address, name, threadID, data, publicClient):
        threading.Thread.__init__(self)
        self._CONECTION = conection
        self._ADDRESS = address
        self.nameThread = name
        self.threadID = threadID
        self.data = data
        self.public_client = publicClient
        self.list = []

    def run(self):
        print('Start thread : ', self._ADDRESS)
        self.init_dispacher()

    def init_dispacher(self):
        continueCon = True
        while continueCon:
            print('Await menssage client : ' + self.nameThread)
            data = self._CONECTION.recv(256)
            if data:
                contunue = self.respose(data)
                if(contunue == 'exit'):
                    continueCon = False

            if(continueCon == False): #FUERZO LA SALIDA
                break

    def respose(self, _data):

        _data = _data.decode()

        if(_data == 'exit'):
            self.closeConnection()
            return 'exit'

        if(_data == "getConnects"):
            self.sendList()
            return 'continue'

        if(_data == "status"):
            self.sendStatus()
            return "continue"

        if(_data != ''):
            send = 'ok'
            self._CONECTION.send(send.encode())

        return 'continue'

    def sendList(self):
        jsonString = self.public_client
        print(jsonString)
        send_packet = self.serializar()
        self._CONECTION.send(send_packet.encode())

    def sendStatus(self):
        sendStatus = "Sending status.!!!"
        self._CONECTION.send(sendStatus.encode())

    def serializar(self):
        return json.dumps(self.public_client)

    def closeConnection(self):
        print('Close disoacher')
        self._CONECTION.close()
        sys.exit()
