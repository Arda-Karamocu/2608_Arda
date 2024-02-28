from machine import Pin, SoftI2C
import ssd1306
from imu import MPU6050
from time import sleep

i2c = SoftI2C(scl=Pin(22), sda=Pin(23))

imu = MPU6050(i2c)

last_s = 0

while True:
    # read in analog value in v
    x = imu.accel.x
    y = imu.accel.y
    z = imu.accel.z
    xg = imu.gyro.x
    yg = imu.gyro.y
    zg = imu.gyro.z
    t = imu.temperature

    
    if -0.2 < x < 0.2 and -0.2 < y < 0.2:
        gyro_status = "centre"
    elif x > 0.4 and -0.2 < y < 0.2 : 
        gyro_status = "right"
    elif x < -0.4 and -0.2 < y < 0.2:
        gyro_status = "left"
    elif y > 0.4 and -0.2 < x < 0.2:
        gyro_status = "front"
    elif y <-0.4 and -0.2 < x < 0.2:
        gyro_status = "behind"
        
    if last_s == gyro_status:
        pass
    else:
        print(gyro_status)
    last_s = gyro_status
    
    
    
    