import nxt
import nxt.locator 
import nxt.brick

bob = nxt.locator.find(host="00:16:53:09:72:DE")
bob.start_program("Bob6.rxe")
MotorLeft = bob.get_motor(nxt.motor.Port.B)
MotorRight = bob.get_motor(nxt.motor.Port.C)
while True:
    msg = bob.message_read(1,0,False)