import machine
from machine import Pin
import time
sw = Pin(36, Pin.IN,Pin.PULL_DOWN)
led = machine.Pin(2, machine.Pin.OUT)

while True:
    if sw.value() == 1:
        led.on()
        time.sleep(0.1)
        led.off()

