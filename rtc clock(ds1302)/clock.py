# Import necessary modules
from ssd1306 import SSD1306_I2C
from machine import Pin, I2C
import ds1302
import time

i2c = I2C(scl=Pin(23), sda=Pin(22))
oled = SSD1306_I2C(128, 64, i2c)

# Initialize DS1302 RTC with specified pins (clk, dio, cs)
ds = ds1302.DS1302(Pin(21),Pin(19),Pin(18))

# Set the date and time on the RTC
#ds.year(2024)  # Set the year to 2085
#ds.month(4)    # Set the month to January
#ds.day(17)     # Set the day to 17th
#ds.hour(21)    # Set the hour to midnight (00)
#ds.minute(30)  # Set the minute to 17
#ds.second(00)  # Set the second to 30


while True:
    oled.fill(0)
    oled.text("Date : ",0,20)
    oled.text("Time : ",0,40)
    oled.text("{}/{}/{}".format(ds.day(), ds.month(),ds.year()),50,20)
    oled.text("{}/{}/{}".format(ds.hour(), ds.minute(),ds.second()),60,40)
    
    print( "Date={}/{}/{}" .format(ds.month(), ds.day(),ds.year()) )
    print( "Time={}:{}:{}" .format(ds.hour(), ds.minute(),ds.second()) )
    oled.show()
    time.sleep(0.5)
