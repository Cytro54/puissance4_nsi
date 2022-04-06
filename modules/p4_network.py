# Ce module se charge de gerer tout ce qui touche
# au réseau. Un (mauvais) systéme de RPC sera 
# implémenté pour faire fonctionner le tout

import json
import socket
import socketserver
from subprocess import call

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

class YuriRPCServerGenericHandler(socketserver.BaseRequestHandler):
    def __init__(self, options):
        super().__init__(self)
        self._opts = options
        self._codec = 'utf-8'

    
    def __attendre_frame(self, socket):
        ## ATTENTION : Cette fonction bloque le thread sur lequel elle est executée
        frame = bytearray()
        while True:
            data = socket.recv(TAILLE_BUFFER)
            if not data:
                break
            else:
                frame.append(data)
        return frame


    def __message_depuis_frame(self, frame):
        return json.load(frame.decode(self._codec))

    def __message_vers_frame(self, message):
        return bytes(json.dump(message), self._codec)


    def handle(self):
        # self.request is the TCP socket connected to the client
        frame = self.__attendre_frame(self.request)
        message = self.__message_depuis_frame(frame)
        # Interpretons le message
        method = message.get('method', None)
        params = message.get('params', None)
        call_id = message.get('id', None)
        if method != None and params != None and call_id != None:
            py_method = f"do_{method}"
            res = self[py_method](*params)
            message = {'id': call_id, 'response': res}
            frame = self.__message_vers_frame(message)
            self.request.sendall(frame)
        else:
            pass
            # Message invalide, droppons le

def init_serveur_rpc(host, port, fonctions):
    with socketserver.TCPServer((host, port), YuriRPCServerHandler) as server:
        server.serve_forever()




if __name__ == "__main__":
    # Quelques Asserts

    # 1. Test de sanité
    message_a_encoder = {'test': 'value', 'cool': 'code'}
    frame = __yuri_rpc_message_vers_frame(message_a_encoder)
    message_decode = __yuri_rpc_message_depuis_frame(frame)
    print("A encoder :")
    print(message_a_encoder)
    print("Décodé :")
    print(message_decode)
    assert message_a_encoder == message_decode
    # 2. 