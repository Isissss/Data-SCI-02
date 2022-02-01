import time
import Adafruit_DHT as dht
import RPi.GPIO as GPIO

# Initialize the sensor with GPIO 13
DHT_SENSOR = dht.DHT11
DHT_PIN = 13


# Set GPIO mode to use GPIO names rather than absolute pin number
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)


while True:
    humidity, temperature = dht.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print(
            "Temperature = {0:0.1f}C  Humidity = {1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor failure. Check wiring.")
    time.sleep(3.0)
