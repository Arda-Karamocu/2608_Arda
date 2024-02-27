from servo import Servo
from machine import Pin
import time

motor_pin = 23
motor = Servo(motor_pin)

buton1 = Pin(22, Pin.IN)
buton2 = Pin(21, Pin.IN)

buton1_status = "off"
buton2_status = "off"

while True:
    if buton1.value() == 1 :
        buton1_status = "on"
  
    else:
        buton1_status = "off"
        
    if buton2.value() == 1:
        buton2_status = "on"

    else:
        buton2_status = "off"
    
    if buton1_status == "on":
        motor.write_angle(180)
        
    elif buton2_status == "on":
        motor.write_angle(0)
    else:
        pass
