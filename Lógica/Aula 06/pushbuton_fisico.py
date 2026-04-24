import machine
from machine import Pin
from time import sleep

led = Pin(18, Pin.OUT)
botao = Pin(21, Pin.IN, Pin.PULL_DOWN)
led1 = Pin(22, Pin.OUT)
botao1 = Pin(23, Pin.IN, Pin.PULL_DOWN)


while 0:
  led.value(1)
  sleep(1)
  led.value(0)
  sleep(1)

while 0:
  estado_botao = botao.value()
  
  sleep(0.2)
  if estado_botao == 1:
    print("")


while 1:
  estado_botao = botao.value()
  if estado_botao == 1:
    estado_led = led.value()
    if estado_led == 1:
      led.value(0)
    else:
      led.value(1)


    sleep(0.1)
    
    
    