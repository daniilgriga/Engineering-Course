import RPi.GPIO as GPIO

GPIO.setwarnings (False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)

def DecimalToBinary (num):
    return [(num >> i) & 1 for i in range (7, -1, -1)]


try:
    while True:

        num = input ("Enter a number:")

        try:
            num = int(num)

            if 0 <= num <= 255:
                GPIO.output (dac, DecimalToBinary (num))

                voltage = (float (num) / 256.0 * 3.3)
                print (f"Out voltage approximately equal {voltage:.4} volt")
            else:
                if num < 0:
                    print ("number have to >= 0, maybe try again")
                elif num > 255:
                    print ("number not in [0, 255], maybe try again")

        except Exception:
            if num == "n": break
            print ("you have to put a int number maybe try again")

finally:
    GPIO.output (dac, 0)
    GPIO.cleanup ()
    print ("bye bye")
                
                