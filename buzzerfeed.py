#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)

def morsecode ():

	#Dot Dot Dot
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.1)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.1)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)

	#Dash Dash Dah
	GPIO.output(22,GPIO.LOW)
	time.sleep(.2)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.2)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.2)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.2)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.2)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.2)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.2)

	#Dot Dot Dot
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.1)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.1)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.7)
	
os.system('clear')
#loop_count = int(input("How many times would you like SOS to loop?: "))
loop_count = 2
while loop_count > 0:
	loop_count = loop_count - 1
	morsecode ()
