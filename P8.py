import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
try:
    while True:
        z = 0
        GPIO.setup(23, GPIO.OUT)
        GPIO.output(23, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.setup(23, GPIO.IN)

        while GPIO.input(23):
            z = z + 1

        num = z / 100
        print(num)
        time.sleep(5)
except KeyboardInterrupt:
    print("Saliendo del programa")
    GPIO.cleanup()
