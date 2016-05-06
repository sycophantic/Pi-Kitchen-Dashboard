#!/usr/bin/python

import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, 1)

global oldtime
global screen
oldtime = time.time()
screen = 1

def motion(channel):
  print "turning screen on"
  GPIO.output(23, 1)
  global oldtime
  oldtime = time.time()
  global screen
  screen = 1

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(24, GPIO.RISING, callback=motion, bouncetime=300)

while True:
  time.sleep(1)
  if time.time() - oldtime > 600:
    if(screen):
      print "turning screen off"
      GPIO.output(23, 0)
      screen = 0
