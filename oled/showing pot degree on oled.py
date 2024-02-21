#You must load the ssd1306.py library to your device

from machine import Pin, SoftI2C, ADC
import ssd1306 #the library
import time

pot = ADC(Pin(36))
pot.width(ADC.WIDTH_10BIT)
pot.atten(ADC.ATTN_11DB)

i2c = SoftI2C(scl=Pin(22), sda=Pin(23))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    oled.fill(0)
    oled.text("---Degrees---",15,0)
    oled.text("pot: ",40,30)
    oled.text(str(pot.read()),70,30)
    oled.show()
    time.sleep(0.1)


    