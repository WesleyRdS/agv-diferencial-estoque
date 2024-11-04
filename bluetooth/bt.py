import nxt
import nxt.locator
import nxt.motor
import time
from nxt.bluetooth import Bluetooth

bob = nxt.locator.find(host="00:16:53:09:72:DE")
bob.start_program("bt2.rxe")

bt = Bluetooth(bob)

def receive_message():
    while True:
        try:
            message = bt.read()  
            print("Recebido:", message)
  
        except Exception as e:
            print("Erro ao receber a mensagem:", e)

receive_message()