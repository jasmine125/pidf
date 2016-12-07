# -*- coding: utf-8 -*-
"""play.py

This module's name is 'play'.
Please use this module for playing image files.
You must install the fbi(framebuffer imageviewer).
 - how to install fbi: apt-get install fbi

"""
import RPi.GPIO as GPIO
import time
import os
import constant


# main function
if __name__ == "__main__":

    GPIO.setmode(GPIO.BCM)
    PIR_PIN = 7

    GPIO.setup(PIR_PIN, GPIO.IN)
    
    # kill a previous fbi process.
    os.system('sudo pkill fbi')

    # execute the fbi.
    os.system('sudo fbi -a -T 2 -t 30 -noverbose `find ./images -iname "*.jpg"`')

    try:
        print 'PIR Module Test (CTRL+C to exit)'
        time.sleep(2)
        print 'Ready'

        while True:
            pirVal = GPIO.input(PIR_PIN)
            if pirVal == True:
                t = time.localtime()
                print '%d:%d:%d motion detected!' % (t.tm_hour, t.tm_min, t.tm_sec)
                os.system('sudo bash -c "echo 0 > /sys/class/backlight/rpi_backlight/bl_power"')
                time.sleep(constant.CONST_BACKLIGHT_TURN_ON_TIME)

            else:
                print 'No motion!!'
                os.system('sudo bash -c "echo 1 > /sys/class/backlight/rpi_backlight/bl_power"')
                time.sleep(constant.CONST_BACKLIGHT_TURN_OFF_TIME)
        
            priVal = False

    except KeyboardInterrupt:
        print 'Quit'
        GPIO.cleanup()

    finally:
        os.system('sudo bash -c "echo 0 > /sys/class/backlight/rpi_backlight/bl_power"')
       

