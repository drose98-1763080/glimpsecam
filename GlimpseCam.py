# This program takes a picture when the button is pressed once
# and a 10 seconds video when pressed twice. Both are saved to /home/pi/
# Pressing and holding the button will result in a single press.

import RPi.GPIO as GPIO
import time
import datetime
from picamera import PiCamera
from time import sleep

camera = PiCamera()

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)

currentState = False
prevState = False
picture = False

while True:
	currentState = not GPIO.input(14)
	if (currentState and not prevState):
		print('single press, waiting for double')
		picture = True
		sleep(.01)
		prevState = currentState
		endtime = time.time() + 1
		while time.time() < endtime:
			currentState = not GPIO.input(14)
			if (currentState and not prevState):
				print('double press')
				picture = False
				sleep(0.01)
				break
			prevState = currentState
			sleep(.01)
		if picture:
			camera.start_preview()
			print('say cheese')
			sleep(5)
			camera.capture('/home/pi/test.png')
			camera.stop_preview()
		else:
	  	        camera.start_preview()
                        camera.start_recording('/home/pi/test.h264')
			print('recording')
                        sleep(10)
                        camera.stop_recording()
                        camera.stop_preview()
	prevState = currentState
	sleep(.01)