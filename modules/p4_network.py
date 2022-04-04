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
        data = socket.recv(TAILLE_BUFFER)
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
    for b in frame:
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
            key_buffer = line
        else: 
            message.update({key_buffer: line})
        is_key = not is_key
    return message

def __yuri_rpc_message_vers_frame(message):
    stream = bytearray()
    i = len(message)
    y = 1
    for key in message:
        # Ajouter une ligne
        stream += bytes(key, 'utf-8')
        stream += SEPARATEUR
        stream += bytes(message[key], 'utf-8')
        if not (i == y):
            stream += SEPARATEUR
            y += 1
    return stream

class YuriRPCClient:
    def __init__(self):
        pass
    
    async def connecter(self, addresse):
        pass

    async def appler(self, nom, parametres):
        pass
class YuriRPCServer:
    def __init__(self):
        pass

    async def ecouter(self, port):
        pass

    def ajouter_fn(self, nom, fonction):
        pass

if __name__ == "__main__":
    # Quelques Asserts
    message_a_encoder = {'test': 'value', 'cool': 'code'}
    frame = __yuri_rpc_message_vers_frame(message_a_encoder)
    message_decode = __yuri_rpc_message_depuis_frame(frame)
    print(message_a_encoder)
    print(message_decode)
    assert message_a_encoder == message_decode
       