from time import sleep
import machine
from machine import Pin


led = Pin(18, Pin.OUT)
led1 = Pin(2, Pin.OUT)
led2 = Pin(4, Pin.OUT)

while 1:
    led.value(1)
    sleep(0.5)
    led.value(0)
    led1.value(1)
    sleep(0.5)
    led1.value(0)
    led2.value(1)
    sleep(0.5)
    led2.value(0)