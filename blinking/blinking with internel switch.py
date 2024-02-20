from machine import Pin
import time
sw = Pin(0, Pin.IN)
led = Pin(23, Pin.OUT)

while True:
    if sw.value() == 0:
        led.on()
    else:
        led.off()
