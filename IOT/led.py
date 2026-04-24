from machine import Pin, ADC, time_pulse_us
from time import sleep, ticks_ms, ticks_diff
from machine import I2C, Pin, SoftI2C
from I2C import I2cLcd

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000) # connect scl to GPIO 22, sda to GPIO 21
lcd = I2cLcd(i2c, 0x27, 2, 16)


while 1: # lcd print
    lcd.move_to(0,0)
    lcd.putstr('Ola')
    lcd.move_to(0,1)
    lcd.putstr('mundo')
    sleep(1)
    lcd.clear()
    

    sleep(0.025)
    lcd.move_to(0,0)
    lcd.putstr(f"pot:")
    sleep(3)
    lcd.clear()

