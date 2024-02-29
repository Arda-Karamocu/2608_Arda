from mfrc522 import MFRC522
from machine import Pin
from machine import SPI

red = Pin(14, Pin.OUT)
grn = Pin(13, Pin.OUT)

spi = SPI(2, baudrate=2500000, polarity=0, phase=0)
spi.init()
rdr = MFRC522(spi=spi, gpioRst=4, gpioCs=5)

print("Place card")


while True:
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            
            card_id = "0x%02x%02x%02x%02x" %(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            print("UID:", card_id)
            
            if card_id == "0xb3da3e40":
                grn.value(True)
                red.value(False)
            else:
                grn.value(False)
                red.value(True)
