import smbus
import time
import sys
bus = smbus.SMBus(1);
DEVICE = 0x21 # Device address
IODIRA = 0x00 # Pin direction register
IODIRB = 0x01
OLATA  = 0x14 # Register for outputs
OLATB  = 0x15
GPIOA  = 0x12 # Register for inputs
GPIOB  = 0x13

# set all I/O to output direction
bus.write_byte_data(DEVICE, IODIRA, 0x00)
bus.write_byte_data(DEVICE, IODIRB, 0x00)

digits = (
    0xC0,
    0xF9,
    0xA4,
    0xB0,
    0x99,
    0x92,
    0x82,
    0xF8,
    0x80,
    0x90,
    0x7F
)

number = int(sys.argv[1])
print(number)
while number >= 0:
    bus.write_byte_data(DEVICE, OLATA, digits[number/10])
    bus.write_byte_data(DEVICE, OLATB, digits[number%10])
    time.sleep(1)
    number -= 1
