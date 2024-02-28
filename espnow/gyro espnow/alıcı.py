import network
import espnow
from machine import Pin, SoftI2C
import ssd1306
import time

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)

# Initialize ESP-NOW
esp = espnow.ESPNow()
esp.active(True)

i2c = SoftI2C(scl=Pin(22), sda=Pin(23))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    _,msg = esp.recv()
    print(msg)
    oled.fill(0)
    oled.text("---Status---",15,0)
    oled.text(msg,40,30)
    oled.show()
