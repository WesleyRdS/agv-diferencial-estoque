import nxt
import nxt.locator
import nxt.motor
import time
from nxt.backend.bluetooth import Backend

bob = nxt.locator.find(host="00:16:53:09:72:DE")
bob.start_program("bt.rxe")

bt = Backend(bob)

def receive_message():
    while True:
        try:
            message = bt.read()  
            print("Recebido:", message)
           
            if message.startswith("B:"):
                parts = message.split()
                counterB = int(parts[0].split(':')[1])
                counterC = int(parts[1].split(':')[1])
                print(f"Contador do Motor B: {counterB}, Contador do Motor C: {counterC}")
        except Exception as e:
            print("Erro ao receber a mensagem:", e)

receive_message()