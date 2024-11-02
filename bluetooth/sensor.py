import time

import nxt.locator
import nxt.sensor

import nxt.sensor.generic

#teste - ultrassonico
with nxt.locator.find(host="00:16:53:09:72:DE") as b:
    mysensor = b.get_sensor(nxt.sensor.Port.S4) #verificar se o sensor ta nessa porta
    print("Use Ctrl-C to interrupt")
    while True:
        distance_cm = mysensor.get_sample()
        print(distance_cm)
        time.sleep(0.5) 
        