from machine import Pin, ADC, PWM
import time

led = PWM(Pin(23))
pot = ADC(Pin(36))
pot.width(ADC.WIDTH_10BIT)
pot.atten(ADC.ATTN_11DB)
led.freq(1000)
while True:
    led.duty_u16(pot.read_u16())
    