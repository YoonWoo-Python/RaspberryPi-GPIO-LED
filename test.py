import RPi.GPIO as gpio
import time 

gpio.setmode(gpio.BCM)

LED_pin = 2
gpio.setup(LED_pin, gpio.OUT) 

try:
    while True:
        gpio.output(LED_pin, gpio.HIGH)
        time.sleep(1)
        gpio.output(LED_pin, gpio.LOW)
        time.sleep(1)

finally: 
    gpio.cleanup()