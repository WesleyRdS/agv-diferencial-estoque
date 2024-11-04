import nxt
import nxt.locator
import nxt.motor
import time
from nxt.backend.bluetooth import Backend

bluetooth_backend = Backend()
bob = nxt.locator.find(host="00:16:53:09:72:DE", backend=bluetooth_backend)

if bob:
    print("Conectado ao robô NXT.")
    bob.start_program("bt2.rxe")
    bluetooth_sock = bob.bluetooth

    def receive_message():
        while True:
            try:
                message = bluetooth_sock.recv()
                message = message.decode('utf-8').strip()
                print("Recebido:", message)

            except Exception as e:
                print("Erro ao receber a mensagem:", e)

    receive_message()

else:
    print("Robô NXT não encontrado.")
