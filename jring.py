#!/usr/bin/env python
# script by Jacch Chen https://jacch.php5.idv.tw
import RPi.GPIO as GPIO
import time,sys,os

#開啟樹苺派GPIO
GPIO.setmode(GPIO.BCM)

#使用GPIO電力
GPIO.setup(17, GPIO.OUT)

#開啟基本電源
GPIO.output(17, 1)

while True:
    #如果發生短路就播放音效
    if not GPIO.input(17):
        os.system('aplay /home/pi/0.wav')
        print "有人來了"
        time.sleep(2)

    time.sleep(1)