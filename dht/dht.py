from machine import Pin
from time import sleep
import dht 

sensor = dht.DHT11(Pin(14))

while True:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print("Temperature:",temp,"°C")
    print("Humidity: %",hum)