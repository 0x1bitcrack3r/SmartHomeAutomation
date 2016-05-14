import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24, GPIO.OUT)
#print "pin 24 off" 
GPIO.output(24, GPIO.HIGH)

