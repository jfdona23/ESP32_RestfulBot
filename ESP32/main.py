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

# API definitions
url = 'http://192.168.0.90:8080/v1/outbound'
method = 'POST'
lastHash = 0

def blinkLed(led, onTime, offTime, blinks):     # Useful function to control led blinking.
    for _ in range(blinks):                     # Parameters are:
        led.value(not led.value())              # - The led to control as a Pin object.
        sleep(onTime)                           # - The ON time in seconds
        led.value(not led.value())              # - The OFF time in seconds
        sleep(offTime)                          # - The amount of blinks.

def getUrl(method, url, data=None, json=None, headers={}):
    r = request(method, url, data, json, headers)
    j = r.json()
    r.close()
    return j

def pickOrder(order):
    switch = {
        "forward": motion.forward,
        "backward": motion.backward,
        "left": motion.left,
        "right": motion.right,
        "stop": motion.stop
    }
    return switch.get(order)


# Main loop
while sonar.distance_cm > 15:
    try:
        r = getUrl(method, url)
    except:
        blinkLed(ledRed, 0.5, 0.3, 2)
        pass
    if lastHash != r['hash']:
        pickOrder(r['order'])()
        sleep(r['argument'])
        lastHash = r['hash']
    else:
        pass

motion.stop()
from machine import soft_reset
soft_reset()