from machine import Pin, ADC
from time import sleep

x = ADC(Pin(39))
y = ADC(Pin(36))
x.width(ADC.WIDTH_10BIT)
x.atten(ADC.ATTN_11DB)
y.width(ADC.WIDTH_10BIT)
y.atten(ADC.ATTN_11DB)

while True:
    print("x =",x.read(),"- y =",y.read())
    sleep(0.2)

        
