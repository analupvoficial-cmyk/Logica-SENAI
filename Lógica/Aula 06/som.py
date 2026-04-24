from machine import Pin, PWM, ADC
from time import sleep

pot0 = ADC(Pin(34))  # Define o pino 34 como entrada analógica

pot0.atten(ADC.ATTN_11DB)  
pot0.width(ADC.WIDTH_10BIT)  


pino_buzzer = Pin(4)
buzzer = PWM(pino_buzzer)

  



while True:
    sleep(0.5)
    buzzer.duty(0)
    buzzer.freq(400)  
    buzzer.duty(512)         
    sleep(0.5)
    pot_value0 = pot0.read()  
    print(f"pot value0 : {pot_value0}")
    print(pot_value0)
    
