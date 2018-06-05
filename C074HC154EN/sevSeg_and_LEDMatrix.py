import RPi.GPIO as GPIO
import smbus
import time
import sys

bus = smbus.SMBus(1);
DEVICE = (0X20, 0X21) # Device address: 20 for LED Matrix, 21 for Sev-seg
IODIRA = 0x00 # Pin direction register
IODIRB = 0x01
OLATA  = 0x14 # Register for outputs
OLATB  = 0x15
GPIOA  = 0x12 # Register for inputs
GPIOB  = 0x13
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

digits = (
    0xC0, #0
    0xF9, #1
    0xA4, #2
    0xB0, #3
    0x99, #4
    0x92, #5
    0x82, #6
    0xF8, #7
    0x80, #8
    0x90, #9
    0x7F  #.
)

#            1g  1r  2g  2r  3g  3r  4g  4r  5g 5r 6g  6r  7g  7r  8g  8r
# cathode = (26, 29, 23, 24, 21, 22, 18, 19, 7, 8, 10, 11, 12, 13, 15, 16)
cathode = (7, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 29, 31, 32)

# 4-to-16 decoder
A = (11, 12, 13, 15)	# A0 ~ A3
enable = (16, 18)		# E2, E1


def busWrite(device, olata, olatb):
    bus.write_byte_data(device, OLATA, olata)
    bus.write_byte_data(device, OLATB, olatb)

def switchForGreen(index):
    switch = {
        0: (0x0A, 0x00),
        1: (0x2A, 0x40),
        2: (0x0A, 0x00),
        3: (0x02, 0x50),
        4: (0x0A, 0x44),
        5: (0x22, 0x44),
        6: (0x02, 0x10),
        7: (0x28, 0x04)
    }
    return switch.get(index, "Not Found!")

def switchForRed(index):
    switch = {
        0: (0x01, 0x80),
        1: (0x05, 0xA0),
        2: (0x01, 0x80),
        3: (0x05, 0xA0),
        4: (0x11, 0x88),
        5: (0x11, 0x88),
        6: (0x04, 0x20),
        7: (0x14, 0x28)
    }
    return switch.get(index, "Not Found!")

def displayLittleMan(color):
    # loop 100 times (about 1 second), but it should be 250 times   (very strange!!!!!!!)
    for counter in range(100):
        # 8 rows
        for row in range(8):
            if color == "green":
                olata = switchForGreen(row)[0]
                olatb = switchForGreen(row)[1]
                busWrite(DEVICE[0], olata, olatb)
                GPIO.output(cathode[2*row], GPIO.LOW)
                time.sleep(0.0005)
                GPIO.output(cathode[2*row], GPIO.HIGH)
            elif color == "red":
                olata = switchForRed(row)[0]
                olatb = switchForRed(row)[1]
                busWrite(DEVICE[0], olata, olatb)
                GPIO.output(cathode[2*row+1], GPIO.LOW)
                time.sleep(0.0005)
                GPIO.output(cathode[2*row+1], GPIO.HIGH)

def changeColor(color):
    if color == "green":
        return "red"
    elif color == "red":
        return "green"
    
# set all I/O to output direction
for device in DEVICE:
    busWrite(device, 0x00, 0x00)

# disable E1, E2
for e in enable:
    GPIO.setup(e, GPIO.OUT)
    GPIO.output(e, GPIO.HIGH)

# initialize A0~A3
for a in A:
    GPIO.setup(a, GPIO.OUT)
    GPIO.output(a, GPIO.LOW)

# turn LED off
# for n in cathode:
#     GPIO.setup(n, GPIO.OUT)
#     GPIO.output(n, GPIO.HIGH)

# test
# while True:
#     busWrite(DEVICE[0], 0xAA, 0x55)
#     for e in enable:
#         GPIO.output(e, GPIO.LOW)

color  = sys.argv[1]

while True:
    number = int(sys.argv[2])
    while number > 0:
        # seven segment display
        busWrite(DEVICE[1], digits[number/10], digits[number%10])
        number -= 1
        displayLittleMan(color);
    color = changeColor(color)
