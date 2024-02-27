from machine import Pin, SoftI2C
import ssd1306
from time import sleep
import utime
import machine
                                             
 
i2c = SoftI2C(scl=Pin(23), sda=Pin(22)) 
oled=ssd1306.SSD1306_I2C(128,64,i2c,0x3c)
# CONSTANTS
KEY_UP   = const(0)
KEY_DOWN = const(1)
 
keys = [['4', '3', '2', '1'], ['8', '7', '6', '5'], ['12', '11', '10', '9'], ['16', '15', '14', '13']]

cols = [19,18,5,17]
rows = [16,4,2,15]
 
# set pins for rows as outputs
row_pins = [Pin(pin_name, mode=Pin.OUT) for pin_name in rows]
 
# set pins for cols as inputs
col_pins = [Pin(pin_name, mode=Pin.IN, pull=Pin.PULL_DOWN) for pin_name in cols]
 
def init():
    for row in range(0,4):
        for col in range(0,4):
            row_pins[row].value(0)
 
def scan(row, col):
    """ scan the keypad """
 
    # set the current column to high
    row_pins[row].value(1)
    key = None
 
    # check for keypressed events
    if col_pins[col].value() == KEY_DOWN:
        key = KEY_DOWN
    if col_pins[col].value() == KEY_UP:
        key = KEY_UP
    row_pins[row].value(0)
 
    # return the key state
    return key
 
print("starting")
 
# set all the columns to low
init()
 
while True:
    oled.fill(0) 
    for row in range(4):
        for col in range(4):
            key = scan(row, col)
            if key == KEY_DOWN:
                oled.text("Key Pressed: ",10,0)
                print("Key Pressed", keys[row][col])
                oled.text(keys[row][col], 55, 30) # display the character associated with the key press
                oled.show()
                last_key_press = keys[row][col]