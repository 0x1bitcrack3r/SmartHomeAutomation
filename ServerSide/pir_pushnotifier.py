import urllib2
import json
import RPi.GPIO as GPIO
import time
import requests
import mechanize

def sendNotification():
	userdata = {"message": "Intruder Detected"}
        #Enter your raspberry pi IP address
	resp = requests.post('http://1raspberrypi_IP_address/post_pirsensordata.php', params=userdata)
def pushNotification():
        browser = mechanize.Browser() 
        browser.open('https://pushbots.com/auth/login')
        browser.select_form(nr=0)
        #Enter email ID
        browser['email'] = 'Email'
        #Enter password
        browser['password'] = 'Password'
        browser.submit()
        #Enter Pushbots app ID
        browser.open('https://pushbots.com/application/push/Pushbots App ID')
        browser.select_form(nr=0)
        browser['push_message'] = 'Intruder Detected'
        browser.submit()

GPIO.setmode(GPIO.BCM)

# In BCM mode pin 7 is identified by id 4
PIR_PIN = 4
GPIO.setup(PIR_PIN, GPIO.IN)

try:
        print "Reading PIR status"

        while True:
                if GPIO.input(PIR_PIN):
                        print "Motion detected"
                	sendNotification()
                        pushNotification()
                
                else:
                	print "No Intruder"
                time.sleep(2)
except KeyboardInterrupt:
        print "Exit"
        GPIO.cleanup()





