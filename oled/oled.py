#You must load the ssd1306.py library to your device

from machine import Pin, SoftI2C
import ssd1306 #the library
import time

i2c = SoftI2C(scl=Pin(22), sda=Pin(23))

oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.text("Hello World",15,15)
oled.text("Merhaba Dunya",15,45)
        
oled.show()