# Boot File
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from network import WLAN, STA_IF
from credentials import my_wifi
from machine import Pin
from utime import sleep
from gc import collect

wifi = WLAN(STA_IF)
wifi.active(True)
wifi.connect(my_wifi.user, my_wifi.passwd)

led = Pin(2, Pin.OUT)
timeout = 0

# Wait for WiFi to connect
while wifi.isconnected() == False:
        led.value(not led.value())
        sleep(0.5)
        timeout += 1
        if timeout > 120: #Timeout of 60 sec (120 times 0.5 sec)
            from machine import reset
            sleep(1)
            reset()
            

led.value(0)
del led
del timeout
collect()

print('===== My IP Address: =====')
print(wifi.ifconfig())