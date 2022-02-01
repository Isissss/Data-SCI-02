import requests
import time
import Adafruit_DHT as dht
import datetime 
import RPi.GPIO as GPIO

# Initialize the sensor with GPIO 13
DHT_SENSOR = dht.DHT11
DHT_PIN = 13

#API Key for ThingSpeak needed for update call
api_key='MJES7KJYQ9M0QL4E'
# URL for get request, json format so output is visible in the bash
url = 'https://api.thingspeak.com/update.json'

# Set GPIO mode to use GPIO names rather than absolute pin number
GPIO.setmode(GPIO.BCM)
#Disable warnings for now
GPIO.setwarnings(False)

#Define outputs
GPIO.setup(18,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)


def measure():
    try:
        while True:
        # Define humidity and temperature variables
            humidity, temperature = dht.read(DHT_SENSOR, DHT_PIN)
            if humidity is not None and temperature is not None and humidity < 100:
                # Light up the LED status indicator based on humidity value
                status = indicator(humidity); 
                temperature_f = temperature * 9 / 5 + 32;
            
                queries = {'api_key': api_key,'field2': humidity, 'field3' : temperature, 'field6' : status, 'field5' : temperature_f}
                r = requests.get(url, params=queries)
                print ("Temperature(C) = {0:0.1f}C  Humidity = {1:0.1f}% Temperature(F)= {2:0.1f}F ".format(temperature, humidity, temperature_f))
                # Print result. If failed, result will return 0
                print ("Result: ", r.text)
                # White LED to indicate it's succesfully measuring, 15s wait time due to restrictions of ThingSpeak free account
                GPIO.output(18,GPIO.HIGH);
                time.sleep(15)
            else:
                print ("Sensor error!")
                GPIO.output(18,GPIO.LOW);
                time.sleep(3)
    except KeyboardInterrupt:
        # If script is stopped, reset LEDs
        GPIO.cleanup()    
                        
def indicator(humidity): 
    if humidity is not None and humidity < 100:
        # Bad status
        if humidity > 70.0 or humidity < 30:
          status = 3
          GPIO.output(24,GPIO.HIGH);
          GPIO.output(23,GPIO.LOW);
          GPIO.output(21,GPIO.LOW);
          return status
        # Orange value 
        elif humidity > 60.0:  
          status = 2
          GPIO.output(23,GPIO.HIGH);
          GPIO.output(21,GPIO.LOW);
          GPIO.output(24,GPIO.LOW);
          return status
        # Good status
        elif humidity > 30.0:
          status = 1
          GPIO.output(21,GPIO.HIGH);
          GPIO.output(23,GPIO.LOW);
          GPIO.output(24,GPIO.LOW);
          return status
        
if __name__ == '__main__':
    measure()
