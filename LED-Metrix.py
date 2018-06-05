import smbus
import RPi.GPIO as GPIO
import time
import sys

bus = smbus.SMBus(1);
DEVICE = 0x20 # Device address
IODIRA = 0x00 # Pin direction register
IODIRB = 0x01
OLATA  = 0x14 # Register for outputs
OLATB  = 0x15
GPIOA  = 0x12 # Register for inputs
GPIOB  = 0x13
color  = sys.argv[1]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#          1g  1r  2g  2r  3g  3r  4g  4r  5g 5r 6g  6r  7g  7r  8g  8r
cathode = (26, 29, 23, 24, 21, 22, 18, 19, 7, 8, 10, 11, 12, 13, 15, 16)

# turn off
for n in cathode:
    GPIO.setup(n, GPIO.OUT)
    GPIO.output(n, GPIO.HIGH)

# set all I/O to output direction
bus.write_byte_data(DEVICE, IODIRA, 0x00)
bus.write_byte_data(DEVICE, IODIRB, 0x00)

if color == "green":
    while True:
        # row 1
        bus.write_byte_data(DEVICE, OLATA, 0x0A)
        bus.write_byte_data(DEVICE, OLATB, 0x00)
        GPIO.output(cathode[0], GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(cathode[0], GPIO.HIGH)
        # row 2
        bus.write_byte_data(DEVICE, OLATA, 0x2A)
        bus.write_byte_data(DEVICE, OLATB, 0x40)
        GPIO.output(cathode[2], GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(cathode[2], GPIO.HIGH)
        # row 3
        bus.write_byte_data(DEVICE, OLATA, 0x0A)
        bus.write_byte_data(DEVICE, OLATB, 0x00)
        GPIO.output(cathode[4], GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(cathode[4], GPIO.HIGH)
        # row 4
        bus.write_byte_data(DEVICE, OLATA, 0x02)
        bus.write_byte_data(DEVICE, OLATB, 0x50)
        GPIO.output(cathode[6], GPIO.LOW)
        time.sleep(0.0001)
        GPIO.output(cathode[6], GPIO.HIGH)
        # row 5
        bus.write_byte_data(DEVICE, OLATA, 0x0A)
        bus.write_byte_data(DEVICE, OLATB, 0x44)
        GPIO.output(cathode[8], GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(cathode[8], GPIO.HIGH)
        # row 6
        bus.write_byte_data(DEVICE, OLATA, 0x22)
        bus.write_byte_data(DEVICE, OLATB, 0x44)
        GPIO.output(cathode[10], GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(cathode[10], GPIO.HIGH)
        #row 7
        bus.write_byte_data(DEVICE, OLATA, 0x02)
        bus.write_byte_data(DEVICE, OLATB, 0x10)
        GPIO.output(cathode[12], GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(cathode[12], GPIO.HIGH)
        #row 8
        bus.write_byte_data(DEVICE, OLATA, 0x28)
        bus.write_byte_data(DEVICE, OLATB, 0x04)
        GPIO.output(cathode[14], GPIO.LOW)
        time.sleep(0.0001)
        GPIO.output(cathode[14], GPIO.HIGH)
elif color == "red":
    while True:
        # row 1
        bus.write_byte_data(DEVICE, OLATA, 0x01)
        bus.write_byte_data(DEVICE, OLATB, 0x80)
        GPIO.output(cathode[1], GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(cathode[1], GPIO.HIGH)
        # row 2
        bus.write_byte_data(DEVICE, OLATA, 0x05)
        bus.write_byte_data(DEVICE, OLATB, 0xA0)
        GPIO.output(cathode[3], GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(cathode[3], GPIO.HIGH)
        # row 3
        bus.write_byte_data(DEVICE, OLATA, 0x01)
        bus.write_byte_data(DEVICE, OLATB, 0x80)
        GPIO.output(cathode[5], GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(cathode[5], GPIO.HIGH)
        # row 4
        bus.write_byte_data(DEVICE, OLATA, 0x05)
        bus.write_byte_data(DEVICE, OLATB, 0xA0)
        GPIO.output(cathode[7], GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(cathode[7], GPIO.HIGH)
        # row 5
        bus.write_byte_data(DEVICE, OLATA, 0x11)
        bus.write_byte_data(DEVICE, OLATB, 0x88)
        GPIO.output(cathode[9], GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(cathode[9], GPIO.HIGH)
        # row 6
        bus.write_byte_data(DEVICE, OLATA, 0x11)
        bus.write_byte_data(DEVICE, OLATB, 0x88)
        GPIO.output(cathode[11], GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(cathode[11], GPIO.HIGH)
        #row 7
        bus.write_byte_data(DEVICE, OLATA, 0x04)
        bus.write_byte_data(DEVICE, OLATB, 0x20)
        GPIO.output(cathode[13], GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(cathode[13], GPIO.HIGH)
        #row 8
        bus.write_byte_data(DEVICE, OLATA, 0x14)
        bus.write_byte_data(DEVICE, OLATB, 0x28)
        GPIO.output(cathode[15], GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(cathode[15], GPIO.HIGH)
#turnoff(cathode)


