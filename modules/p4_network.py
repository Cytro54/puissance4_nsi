# Ce module se charge de gerer tout ce qui touche
# au réseau. Un (mauvais) systéme de RPC sera 
# implémenté pour faire fonctionner le tout

import json
import socket
import socketserver
from subprocess import call
import threading

TAILLE_BUFFER = 1024
SEPARATEUR = b'&'
SEPARATEUR_INT = 38


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

def __message_depuis_frame(frame):
    return json.load(frame.decode(CODEC))

def __message_vers_frame(message):
    string = json.dumps(message)
    return bytes(string, CODEC)

def __attendre_frame(socket):
    ## ATTENTION : Cette fonction bloque le thread sur lequel elle est executée
    frame = bytearray()
    while True:
        data = socket.recv(TAILLE_BUFFER)
        if not data:
            break
        else:
            frame.append(data)
    return frame 

class YuriRPCServerGenericHandler(socketserver.BaseRequestHandler):
    def __init__(self, options):
        super().__init__(self)
        self._opts = options
        self._codec = 'utf-8'

    def handle(self):
        # self.request is the TCP socket connected to the client
        frame = __attendre_frame(self.request)
        message = __message_depuis_frame(frame)
        # Interpretons le message
        method = message.get('method', None)
        params = message.get('params', None)
        call_id = message.get('id', None)
        if method != None and params != None and call_id != None:
            py_method = f"do_{method}"
            res = self[py_method](*params)
            message = {'id': call_id, 'response': res}
            frame = __message_vers_frame(message)
            self.request.sendall(frame)
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
        frame = __message_vers_frame(message_a_encoder)
        self._socket.sendall(frame)

        # (On attend que ca bosse)

        # 2. Attendre le message retour
        frame = __attendre_frame(self._socket)
        message = __message_depuis_frame(frame)

        # 3. Interpretons le message
        reponse = message.get('reponse', None)
        call_id = message.get('id', None)
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
            server.serve_forever()


if __name__ == "__main__":
    # Quelques Asserts

    # 1. Test de sanité
    message_a_encoder = {'test': 'value', 'cool': 'code'}
    frame = __message_vers_frame(message_a_encoder)
    message_decode = __message_depuis_frame(frame)
    print("A encoder :")
    print(message_a_encoder)
    print("Décodé :")
    print(message_decode)
    assert message_a_encoder == message_decode
    
    # 2. Tests + Avancés

    class TestYuriRPCServer(YuriRPCServerGenericHandler):
        def do_ping():
            return 'pong'

        def do_echo(message):
            return message

    server_thread = YuriRPCServerThread('0.0.0.0', 9999, TestYuriRPCServer)
    server_thread.start()
    
    client = YuriRPCClient('localhost', 9999)
    assert client.call('ping', []) == 'pong'