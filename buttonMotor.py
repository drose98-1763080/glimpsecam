from gpiozero import Button
import time
from time import sleep
import RPi.GPIO as GPIO

button1 = Button(2)
button2 = Button(4)

GPIO.setup(3, GPIO.OUT)
GPIO.output(3,False)

while True:
    if button1.is_pressed:
        GPIO.output(3, True)
        sleep(1)
        GPIO.output(3, False)
    if button2.is_pressed:
        GPIO.output(3, True)
        sleep(0.5)
        GPIO.output(3, False)
        sleep(0.5)
        GPIO.output(3, True)
        sleep(0.5)
        GPIO.output(3, False)
        sleep(0.5)
