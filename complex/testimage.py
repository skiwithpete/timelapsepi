#!/usr/bin/python
# BEFORE USING THIS SCRIPT.
# mkdir ~/timelapse 
# mkdir ~/timelapse/completed
# this file should live in ~/timelapse and is run with command "python ~/timelapse/timelapse.py

import time
from picamera import PiCamera
from os import system

camera = PiCamera()
camera.resolution = (960,540)
# my camera was flipped and upside down - this fixes that
camera.vflip = True
camera.hflip = True

camera.capture('imagetest.jpeg')


print('done')

