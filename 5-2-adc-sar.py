import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = 0)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = 1)

def dec2bin(num):
    return [int(bin) for bin in bin(num)[2:].zfill(8)]

def comparator(value_res):
    value = dec2bin(value_res)
    GPIO.output(dac, value)
    time.sleep(0.01)
    return GPIO.input(comp)

def adc():
    start = time.time()

    result = 128

    if(comparator(result) == 1): result -= 128
    result +=64

    if(comparator(result) == 1): result -= 64
    result += 32
    
    if(comparator(result) == 1): result -= 32
    result += 16

    if(comparator(result) == 1): result -= 16
    result += 8

    if(comparator(result) == 1): result -= 8
    result += 4

    if(comparator(result) == 1): result -=4
    result += 2

    if(comparator(result) == 1): result -= 2
    result += 1

    if(comparator(result) == 1): result -= 1
        
    dtime = time.time() - start

    return [result, dtime]

try:
    while True:
        results = adc()
        voltage = results[0] * 3.3 / 256
        binary_value = ''.join(map(str, dec2bin(results[0])))
        print(f'DEX: {results[0]}, BIN: {binary_value}, Voltage: {voltage} V, Time: {results[1]:} с')
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()