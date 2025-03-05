import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2, 3, 4, 17, 27, 22, 10, 9][::-1]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = 0)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(led, GPIO.OUT)

def dec2bin(num):
    return [int(bin) for bin in bin(num)[2:].zfill(8)]


def adc():
    volumes = [0, 1, 3, 7, 15, 31, 63, 127, 255]
    d = [i * 32 for i in range(9)]

    result = 0

    check = [0 for i in range(8)]

    for i in range(8):
        check[i] = 1

        GPIO.output(dac, check)
        time.sleep(0.01)

        if GPIO.input(comp) == 0:
            result += 2**(7 - i)
        else:
            check[i] = 0

    volumes_d = [abs(i - result) for i in d]
    print(result*(3.3/256), volumes_d)

    return volumes[volumes_d.index(min(volumes_d))]


try:
    while True:
        GPIO.output(led, dec2bin(adc()))
        print(adc())

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()