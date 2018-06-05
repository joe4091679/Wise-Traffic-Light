#import RPi.GPIO as GPIO
import smbus
import time

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(3, GPIO.OUT)
#GPIO.output(3, GPIO.LOW)
#GPIO.setup(5, GPIO.OUT)
#GPIO.output(5, GPIO.LOW)
#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1
 
DEVICE = 0x20 # Device address (A0-A2)
IODIRA = 0x00 # Pin direction register
OLATA  = 0x14 # Register for outputs
GPIOA  = 0x12 # Register for inputs
signal = 0x01
 
# Set all GPA pins as outputs by setting
# all bits of IODIRA register to 0
bus.write_byte_data(DEVICE,IODIRA,0x00)
 
# Set output all 7(8?) output bits to 0
bus.write_byte_data(DEVICE,OLATA,0)
while True:
    print signal
    bus.write_byte_data(DEVICE, OLATA, signal)
    signal <<= 1
    if signal > 0x04:
        signal = 0x01
    time.sleep(1)

 
# Set all bits to zero
bus.write_byte_data(DEVICE,OLATA,0)