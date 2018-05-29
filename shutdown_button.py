#!/bin/python

import RPi.GPIO as GPIO
import os
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def Shutdown(channel): 
	os.system("sudo shutdown -h now")
	
GPIO.add_event_detect(4, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)