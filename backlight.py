#!/usr/bin/python

import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, 1)

oldtime = time.time()

def motion(channel):
  print "turning screen on"
  GPIO.output(23, 1)
  oldtime = time.time()

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(24, GPIO.RISING, callback=motion, bouncetime=300)

while True:
  if time.time() - oldtime > 600:
    print "turning screen off"
    GPIO.output(23, 0)
