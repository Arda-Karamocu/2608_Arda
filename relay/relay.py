from machine import Pin

relay1 = Pin(23, Pin.OUT,Pin.PULL_UP)
relay2 = Pin(22, Pin.OUT,Pin.PULL_UP)
sw = Pin(0, Pin.IN)

while True:
    if sw.value() == 0:
        statue = "on"
        relay1.off()
        relay2.off()
    elif sw.value() == 1:
        statue = "off"
        relay1.on()
        relay2.on()
        
