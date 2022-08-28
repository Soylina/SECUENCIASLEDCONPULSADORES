#PRÁCTICA DE LABORATORIO N°2       
       #EJERCICIO N° 1
from machine import Pin as pin
from utime import sleep, sleep_ms
led1=pin(13,pin.OUT)
led2=pin(12,pin.OUT)
led3=pin(14,pin.OUT)
led4=pin(27,pin.OUT)
led5=pin(26,pin.OUT)
led6=pin(25,pin.OUT)
led7=pin(33,pin.OUT)
led8=pin(32,pin.OUT)
amarillo1=pin(15,pin.IN)
para=0.03
def derecha():
        #led 1
    led1.value(1)
    sleep(para)
    led1.value(0)
    sleep(para)
        #Led 2
    led2.value(1)
    sleep(para)
    led2.value(0)
    sleep(para)
        #Led 3
    led3.value(1)
    sleep(para)
    led3.value(0)
    sleep(para)
        #Led 4
    led4.value(1)
    sleep(para)
    led4.value(0)
    sleep(para)
        #Led 5
    led5.value(1)
    sleep(para)
    led5.value(0)
    sleep(para)
        #Led 6
    led6.value(1)
    sleep(para)
    led6.value(0)
    sleep(para)
        #Led 7
    led7.value(1)
    sleep(para)
    led7.value(0)
    sleep(para)
        #Led 8
    led8.value(1)
    sleep(para)
    led8.value(0)
    sleep(para)

while (True):
    if (amarillo1.value()):
        derecha()
        print("si sirvio")
        
    