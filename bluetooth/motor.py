import nxt
import nxt.locator
import nxt.motor  #pra usar motor 

with nxt.locator.find(host="00:16:53:09:72:DE") as b:
    mymotor = b.get_motor(nxt.motor.Port.B) #verificar se eh na porta A mesmo 
    # nxt.backend.devfile.DevFileSock("Bob6.nxc")
    
    
    # #faz um circulo
    # mymotor.turn(25, 360)
    # mymotor.turn(-25, 360)