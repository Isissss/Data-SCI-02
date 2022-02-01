import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
# No warnings
GPIO.setwarnings(False)
#Define outputs
GPIO.setup(18,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
#Leds on
print ( "LED on")
GPIO.output(18,GPIO.HIGH)
GPIO.output(21,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)
GPIO.output(24,GPIO.HIGH)
#Wait 1s
time.sleep(1)
#Leds off
print ( "LED off")
GPIO.output(18,GPIO.LOW)
GPIO.output(21,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
GPIO.output(24,GPIO.LOW)
