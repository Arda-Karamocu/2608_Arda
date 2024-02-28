import network
from machine import Pin, SoftI2C
import espnow
from imu import MPU6050
from time import sleep

i2c = SoftI2C(scl=Pin(22), sda=Pin(23))
imu = MPU6050(i2c)

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)

# Initialize ESP-NOW
esp = espnow.ESPNow()
esp.active(True)

# Define the MAC address of the receiving ESP32 (ESP32 B)
peer =b'\xa0\xa3\xb3(\xc5l'
esp.add_peer(peer)

last_s = 0
while True:
    
    x = imu.accel.x
    y = imu.accel.y
    z = imu.accel.z
    
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
        message = gyro_status
        esp.send(peer, message)
        
    last_s = gyro_status

