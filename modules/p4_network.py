# Ce module se charge de gerer tout ce qui touche
# au réseau. Un (mauvais) systéme de RPC sera 
# implémenté pour faire fonctionner le tout

import json
from random import randint
import socket
import socketserver
from subprocess import call
import sys
import threading
import time
from tkinter import SEPARATOR

TAILLE_BUFFER = 1024



#
# Yuri Rpc ABI:
#
# __key__<s>__value__
#
# Une frame est composée d'une suite de valeurs entrecoupées de separateurs formant une sorte de tableau,
# 
# -> ["foo", "bar", "i_am", "hecker"]
#
# Le tout est transformé en un dict grâce a un algoritme de modulo.
#
# -> {
#   foo: "bar",
#   i_am: "hecker"
# }
# 
CODEC = 'utf-8'
SEPARATOR = b'@@@'

def message_depuis_frame(frame):
    return json.loads(frame.decode(CODEC))

def message_vers_frame(message):
    string = json.dumps(message)
    return bytes(string, CODEC)

def attendre_frame(socket):
    ## ATTENTION : Cette fonction bloque le thread sur lequel elle est executée
    frame = bytearray()
    while True:
        data = socket.recv(TAILLE_BUFFER)
        frame += data
        if frame.endswith(SEPARATOR):
            return frame.replace(SEPARATOR, b'')
        if not data:
            return None

def envoyer_frame(socket, bytes):
    socket.sendall(bytes + SEPARATOR)

class YuriRPCServerGenericHandler(socketserver.BaseRequestHandler):
    def __init__(self, magic1, magic2, magic3):
        socketserver.BaseRequestHandler.__init__(self, magic1, magic2, magic3)
        self._codec = 'utf-8'

    def handle(self):
        while True:
            # self.request is the TCP socket connected to the client
            frame = attendre_frame(self.request)
            message = message_depuis_frame(frame)
            print(message)
            # Interpretons le message
            method = message.get('method', None)
            params = message.get('params', None)
            call_id = message.get('id', None)
            if method != None and params != None and call_id != None:
                py_method = f"do_{method}"
                py_method = getattr(self, py_method)
                if params == []:
                    res = py_method()
                else:
                    res = py_method(*params)
                message = {'id': call_id, 'reponse': res}
                frame = message_vers_frame(message)
                envoyer_frame(self.request, frame)
            else:
                # Message invalide, droppons le
                pass

class YuriRPCClient():
    def __init__(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        self._socket = s
        self._increment = 0

    def call(self, method, parameters):
        self._increment += 1
        
        # 1. Envoyer le message
        message_a_encoder = {'method': method, 'params': parameters, 'id': self._increment}
        frame = message_vers_frame(message_a_encoder)
        envoyer_frame(self._socket, frame)

        # (On attend que ca bosse)

        # 2. Attendre le message retour
        frame = attendre_frame(self._socket)
        if frame is None:
            raise RuntimeError(f"Erreur RPC; (Appel {self._increment}) Connexion casée")
        message = message_depuis_frame(frame)

        # 3. Interpretons le message
        reponse = message.get('reponse', None)
        call_id = message.get('id', None)
        print(message)
        if reponse != None and call_id != None and call_id == self._increment:
            return reponse
        else:
            # Message invalide, droppons le
            pass

class YuriRPCServerThread(threading.Thread):
    def __init__(self, host, port, handler_class):
      threading.Thread.__init__(self)
      self._host = host
      self._port = port
      self._handler_class = handler_class

    def run(self):
        with socketserver.TCPServer((self._host, self._port), self._handler_class) as server:
            server.serve_forever(15)


if __name__ == "__main__":
    # Quelques Asserts

    # 1. Test de sanité
    message_a_encoder = {'test': 'value', 'cool': 'code'}
    frame = message_vers_frame(message_a_encoder)
    message_decode = message_depuis_frame(frame)
    print("A encoder :")
    print(message_a_encoder)
    print("Décodé :")
    print(message_decode)
    assert message_a_encoder == message_decode
    
    # 2. Tests + Avancés

    class TestYuriRPCServer(YuriRPCServerGenericHandler):
        def do_ping(self):
            return 'pong'

        def do_echo(self, message):
            return message

    port = randint(8000, 9000)

    server_thread = YuriRPCServerThread('0.0.0.0', port, TestYuriRPCServer)
    server_thread.start()
    time.sleep(2)
    
    client = YuriRPCClient('localhost', port)
    assert client.call('ping', []) == 'pong'
    assert client.call('echo', ['value']) == 'value'
    print("call réussi")
    sys.exit(0)