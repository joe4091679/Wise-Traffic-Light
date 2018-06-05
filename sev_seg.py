import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

seg1 = (7, 8, 10, 11, 12, 13, 15, 16)
seg2 = (18, 19, 21, 22, 23, 24, 26, 29)
digits = {
    '0': (0, 0, 0, 0, 0, 0, 1, 1),
    '1': (1, 0, 0, 1, 1, 1, 1, 1),
    '2': (0, 0, 1, 0, 0, 1, 0, 1),
    '3': (0, 0, 0, 0, 1, 1, 0, 1),
    '4': (1, 0, 0, 1, 1, 0, 0, 1),
    '5': (0, 1, 0, 0, 1, 0, 0, 1),
    '6': (0, 1, 0, 0, 0, 0, 0, 1),
    '7': (0, 0, 0, 1, 1, 1, 1, 1),
    '8': (0, 0, 0, 0, 0, 0, 0, 1),
    '9': (0, 0, 0, 0, 1, 0, 0, 1),
    '.': (1, 1, 1, 1, 1, 1, 1, 0)
}
for n in range(0, 8):
    GPIO.setup(seg1[n], GPIO.OUT)
    GPIO.setup(seg2[n], GPIO.OUT)
    
number = int(sys.argv[1])
print(number)
for n in range(0, 8):
    GPIO.output(seg2[n], digits[str((0))][n])
    GPIO.output(seg1[n], digits[str((0))][n])
while number >= 0:
    for n in range(0, 8):
        GPIO.output(seg2[n], digits[str(number%10)][n])
        GPIO.output(seg1[n], digits[str(number/10)][n])
    
    number -= 1
    time.sleep(1)