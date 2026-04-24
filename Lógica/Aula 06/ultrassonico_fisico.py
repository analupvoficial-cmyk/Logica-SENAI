import machine
from machine import Pin
from hcsr04 from HCSR04
from time import sleep

led1 = Pin(2, Pin.OUT)
led2 = Pin(4, Pin.OUT)
TRIG = Pin(22)
ECHO = Pin(23)
ultrassonico = HCSR04(trigger_pin=TRIG, echo_pin=ECHO)

freq = 0
dis_cm = 