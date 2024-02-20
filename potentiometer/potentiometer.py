from machine import Pin, ADC
import time

pot = ADC(Pin(36))
pot.width(ADC.WIDTH_10BIT)
pot.atten(ADC.ATTN_11DB)

while True:
    print(pot.read())
    time.sleep(0.2)