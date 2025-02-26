import RPi.GPIO as GPIO
from time import sleep


GPIO.setwarnings (False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)

def DecimalToBinary (num):
    return [(num >> i) & 1 for i in range (7, -1, -1)]

point = 1
t = 0
x = 0

try: 
    period = float (input ("Enter period:"))

    while True:
        GPIO.output (dac, DecimalToBinary (x))
        if   x ==   0: point = 1
        elif x == 255: point = 0
        
        print (f" {x:}")

        x = x + 1 if point == 1 else x - 1

        sleep (period / 512)
        t += 1

except ValueError:
    print ("Strange period....")

finally:
    GPIO.output (dac, 0)
    GPIO.cleanup ()
    print ("bye bye")