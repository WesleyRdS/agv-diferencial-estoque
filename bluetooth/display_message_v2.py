import nxt
import nxt.locator 
import nxt.brick
import time
bob = nxt.locator.find(host="00:16:53:09:72:DE")
bob.start_program("Bob6.rxe")
MotorLeft = bob.get_motor(nxt.motor.Port.B)
MotorRight = bob.get_motor(nxt.motor.Port.C)
r = 2.75
L = 17
OmegaL = 0
OmegaR = 0 
Vxg = 0
TETAg = 0

def separa_elementos(vetor):
    numeros = vetor.strip("()").split(", ")
    numeros = [int(num) for num in numeros]
    return numeros

while True:
    vetorL = MotorLeft.get_tacho().__str__()
    vetorR = MotorRight.get_tacho().__str__()
    Iposition_left = separa_elementos(vetorL)
    print("PIL ", Iposition_left)
    Iposition_right = separa_elementos(vetorR)
    print("PIR ", Iposition_right)
    to = time.clock_gettime_ns(time.CLOCK_REALTIME)
    time.sleep(0.1)
    Fposition_left = separa_elementos(vetorL)
    print("PFL ", Fposition_left)
    Fposition_right = separa_elementos(vetorR)
    print("PFR ", Fposition_right)
    tf = time.clock_gettime_ns(time.CLOCK_REALTIME)
    OmegaL = (Fposition_left[2])/(tf-to)
    OmegaR = (Fposition_right[2])/(tf-to)
    
    Vxg = (((r*OmegaR)/2) + ((r*OmegaL)/2))
    TETAg = (((r*OmegaR)/2*L) - ((r*OmegaL)/2*L))
    print(Vxg)
# print(vetor)separa_elementos(vetorR)