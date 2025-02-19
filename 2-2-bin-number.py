import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)

plt.plot([0, 5, 32, 64, 127, 255], [0.049, 0.1136, 0.458, 0.868, 1.677, 3.255])
plt.show()

dac    = [8, 11, 7, 1, 0, 5, 12, 6]
number = [1,  0, 0, 0, 0, 0,  0, 0]

GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, number)

time.sleep(20)

GPIO.output(dac, 0)
GPIO.cleanup()
