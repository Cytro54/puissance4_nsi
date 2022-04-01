# Ce module se charge de gerer tout ce qui touche
# au réseau. Un (mauvais) systéme de RPC sera 
# implémenté pour faire fonctionner le tout

import socket

TAILLE_BUFFER = 1024
SEPARATEUR = b'\n'

def __yuri_rpc_attendre_frame(socket):
    ## ATTENTION : Cette fonction bloque le thread sur lequel elle est executée
    frame = bytearray()
    while True:
        data = conn.recv(TAILLE_BUFFER)
        if not data: 
            break
        else:
            frame.append(data)
    return frame

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

def __yuri_rpc_decompose_frame(frame):
    buff = bytearray()
    for b in bytes_:
        if b == SEPARATEUR:
            yield buff.decode('utf-8')
            buff = bytearray()
        else:
            buff.append(b)
    if buff:
        yield buff.decode('utf-8') 

def __yuri_rpc_message_depuis_frame(frame):
    is_key = True
    key_buffer = None
    message = {}
    for line in __yuri_rpc_decompose_frame(frame):
        if is_key: 
            keybuf = line
        else: 
            message.update({key_buffer: line})
        is_key = not is_key
    return message

def __yuri_rpc_message_vers_frame(message):
    stream = []
    for key in message:
        # Ajouter une ligne
        stream.append(key)
        stream.append(message[key])
    
    return bytearray(SEPARATEUR.join(stream), 'utf-8')

class YuriRPCClient:
    def __init__(self):

    async def connecter(self, addresse):

    async def appler(self, nom, parametres):

class YuriRPCServer:
    def __init__(self):


    async def ecouter(self, port):

    def ajouter_fn(self, nom, fonction):