import nxt.locator

#acha o dispositivo e printa o nome 
with nxt.locator.find(host="00:16:53:09:72:DE") as b:
    print("Found brick:", b.get_device_info()[0]) 
    b.play_tone(440, 250)
