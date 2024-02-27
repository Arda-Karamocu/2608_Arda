from servo import Servo
from machine import Pin
import time

motor_pin = 23
motor = Servo(motor_pin)

while True:
    motor.write_angle(0)
    time.sleep(1.5)
    motor.write_angle(180)
    time.sleep(1.5)
