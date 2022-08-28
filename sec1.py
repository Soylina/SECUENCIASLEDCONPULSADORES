#PRÁCTICA DE LABORATORIO N°3
#primeras cuatro secuencias
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
amarillo=pin(15,pin.IN)
verde=pin(4,pin.IN)
azul=pin(16,pin.IN)
negro=pin(18,pin.IN)
rojo=pin(19,pin.IN)
para=0.08
pausa=0.40
#Va hacia la derecha
def derecha():
    led1.value(1)
    sleep(para)
    led1.value(0)
    sleep(para)
    led2.value(1)
    sleep(para)
    led2.value(0)
    sleep(para)
    led3.value(1)
    sleep(para)
    led3.value(0)
    sleep(para)
    led4.value(1)
    sleep(para)
    led4.value(0)
    sleep(para)
    led5.value(1)
    sleep(para)
    led5.value(0)
    sleep(para)
    led6.value(1)
    sleep(para)
    led6.value(0)
    sleep(para)
    led7.value(1)
    sleep(para)
    led7.value(0)
    sleep(para)
    led8.value(1)
    sleep(para)
    led8.value(0)
    sleep(para)
#alumbran leds pares    
def derechapares():
    led2.value(1)
    sleep(pausa)
    led2.value(0)
    sleep(pausa)
    led4.value(1)
    sleep(pausa)
    led4.value(0)
    sleep(pausa)
    led6.value(1)
    sleep(pausa)
    led6.value(0)
    sleep(pausa)
    led8.value(1)
    sleep(pausa)
    led8.value(0)
    sleep(pausa)
    
#Va hacia la izquierda  
def izquierda():
    led8.value(1)
    sleep(para)
    led8.value(0)
    sleep(para)
    led7.value(1)
    sleep(para)
    led7.value(0)
    sleep(para)
    led6.value(1)
    sleep(para)
    led6.value(0)
    sleep(para)
    led5.value(1)
    sleep(para)
    led5.value(0)
    sleep(para)
    led4.value(1)
    sleep(para)
    led4.value(0)
    sleep(para)
    led3.value(1)
    sleep(para)
    led3.value(0)
    sleep(para)
    led2.value(1)
    sleep(para)
    led2.value(0)
    sleep(para)
    led1.value(1)
    sleep(para)
    led1.value(0)
    sleep(para)
 #alumbran leds pares    
def izquierdaimpares():
    led7.value(1)
    sleep(pausa)
    led7.value(0)
    sleep(pausa)
    led5.value(1)
    sleep(pausa)
    led5.value(0)
    sleep(pausa)
    led3.value(1)
    sleep(pausa)
    led3.value(0)
    sleep(pausa)
    led1.value(1)
    sleep(pausa)
    led1.value(0)
    sleep(pausa)
  
while (True):
 
        if (azul.value()):
            izquierda()
            print("izquierda")
        elif (amarillo.value()):
            derecha()
            print("derecha")    
        elif (verde.value()):
            derechapares()
            print("derecha pares")
        elif (negro.value()):
            izquierdaimpares()
            print("izquierda impares")    
 
    
                

                
                
            
