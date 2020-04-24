from machine import Pin, PWM
from utime import sleep
from urequests import request
from motors import Motors
from hcsr04 import HCSR04


# LED port definitions
ledBoard = Pin(2, Pin.OUT)
ledRed = Pin(16, Pin.OUT)
ledBlue = Pin(17, Pin.OUT)

# HC-SR04 port definitions
sonar = HCSR04(trigger_pin=25, echo_pin=26)

# Servo motor port definitions
servo1 = PWM(Pin(21), freq=50)  # Duty cycle for my SG09 servo is between 20 - 125. Usual freq for servos is 50Hz.
                                # Detailed info in https://learn.sparkfun.com/tutorials/pulse-width-modulation/all

# DC Motor port definitions
motorLA = Pin(27, Pin.OUT)
motorLB = Pin(14, Pin.OUT)
motorRA = Pin(12, Pin.OUT)
motorRB = Pin(13, Pin.OUT)
motion = Motors(motorRA, motorRB, motorLA, motorLB)
motion.stop() # Ensure the motors are stopped

"""
Useful function to control led blinking.
Parameters are:
- The led to control as a Pin object.
- The ON time in seconds
- The OFF time in seconds
- The amount of blinks.
"""
def blinkLed(led, onTime, offTime, blinks):
    for _ in range(blinks):
        led.value(not led.value())
        sleep(onTime)
        led.value(not led.value())
        sleep(offTime)

def getUrl(method, url, data=None, json=None, headers={}):
    r = request(method, url, data, json, headers)
    j = r.json()
    r.close()
    return j
