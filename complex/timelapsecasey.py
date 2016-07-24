#!/usr/bin/python
# BEFORE USING THIS SCRIPT.
# mkdir ~/timelapse 
# mkdir ~/timelapse/completed
# this file should live in ~/timelapse and is run with command "python ~/timelapse/timelapse.py

import time
from time import sleep
from picamera import PiCamera
from os import system

camera = PiCamera()
camera.resolution = (1920, 1080)
# my camera was flipped and upside down - this fixes that
camera.vflip = True
camera.hflip = True

SleepTimeL = 1
FrameCount = 0
FrameStop = 240

WAIT = int(FrameStop)*int(SleepTimeL)/60

print('starting video now')
camera.start_recording('/home/pi/timelapse/video.h264')
sleep(5)
camera.stop_recording()

print('Photography will take approximately ' + str(WAIT) + ' minutes')
print('Taking photos now')
while (FrameCount < FrameStop):
    print('Picture:' + str(FrameCount) + ' of ' + str(FrameStop))
    camera.capture('/home/pi/timelapse/image' + str(FrameCount).zfill(4) + '.jpg')
    time.sleep(SleepTimeL);
    FrameCount = FrameCount + 1

# create film
print('converting to film now')
system('avconv -i /home/pi/timelapse/video.h264 -c copy /home/pi/timelapse/`date +%Y%m%d%H%M`atimelapse.mp4')
system('avconv -r 24 -i /home/pi/timelapse/image%04d.jpg -vcodec libx264 -crf 20 -g 15 /home/pi/timelapse/`date +%Y%m%d%H%M`btimelapse.mp4')

# create film
print('moving completed mp4 file')
system('mv /home/pi/timelapse/*.mp4 /home/pi/timelapse/completed/')

print('cleaning up old jpgs')
system('rm /home/pi/timelapse/*.h264')
system('rm /home/pi/timelapse/*.jpg')

print('done')
system('shutdown -h now')

