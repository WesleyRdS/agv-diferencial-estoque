import nxt
import nxt.locator 
import nxt.brick
import time

bob = nxt.locator.find(host="00:16:53:09:72:DE")
bob.start_program("Bob6.rxe")
r = 2.75
L = 17
OmegaL = 0
OmegaR = 0 
Vxg = 0
TETAg = 0
while True:
    MotorLeft = bob.get_motor(nxt.motor.Port.B)
    Iposition_left = MotorLeft.get_tacho()
    MotorRight = bob.get_motor(nxt.motor.Port.C)
    IPosition_right = MotorRight.get_tacho()
    to = time.gettime_ns()
    time.sleep(100)
    Fposition_left = MotorLeft.get_tacho()
    Fposition_right = MotorRight.get_tacho()
    tf = time.gettime_ns()
    OmegaL = (Fposition_left - Iposition_left)/(tf-to)
    OmegaR = (Fposition_right - IPosition_right)/(tf-to)
    
    Vxg = (((r*OmegaR)/2) + ((r*OmegaL)/2))
    TETAg = (((r*OmegaR)/2*L) - ((r*OmegaL)/2*L))