#PRÁCTICA DE LABORATORIO N°3
from machine import Pin as pin
from utime import sleep as stop, sleep_ms as para,sleep_us as pausa
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

def print_led(a,b,c,d,e,f,g,h):
        led1.value(a) 
        led2.value(b)
        led3.value(c)
        led4.value(d)
        led5.value(e)
        led6.value(f)
        led7.value(g)
        led8.value(h)
        para(500)
#alumbran todos        
def todos():
                
        print_led(0,0,0,0,0,0,0,0)
        print_led(1,1,1,1,1,1,1,1)
        print_led(0,0,0,0,0,0,0,0)
        print_led(1,1,1,1,1,1,1,1)
        print_led(0,0,0,0,0,0,0,0)
        print_led(1,1,1,1,1,1,1,1)
        print_led(0,0,0,0,0,0,0,0)
        
#encienden uno si otro no        
def unosi():
                
        print_led(0,0,0,0,0,0,0,0)
        print_led(1,0,1,0,1,0,1,0)
        print_led(0,0,0,0,0,0,0,0)
        print_led(1,0,1,0,1,0,1,0)
        print_led(0,0,0,0,0,0,0,0)
        print_led(1,0,1,0,1,0,1,0)
        print_led(0,0,0,0,0,0,0,0)
        
def miti():
        print_led(0,0,0,0,0,0,0,0)
        print_led(1,1,1,1,0,0,0,0)
        print_led(0,0,0,0,0,0,0,0)
        print_led(1,1,1,1,0,0,0,0)
        print_led(0,0,0,0,0,0,0,0)
        print_led(1,1,1,1,0,0,0,0)
        print_led(0,0,0,0,0,0,0,0)
        
def mitad():
        print_led(0,0,0,0,0,0,0,0)
        print_led(0,0,0,0,1,1,1,1)
        print_led(0,0,0,0,0,0,0,0)
        print_led(0,0,0,0,1,1,1,1)
        print_led(0,0,0,0,0,0,0,0)
        print_led(0,0,0,0,1,1,1,1)
        print_led(0,0,0,0,0,0,0,0)
                
        
        
while (True):
 
        if (amarillo.value()):
         todos()
         print("todos")
        elif (verde.value()):
             unosi()
             print("unosi")
        elif (azul.value()):
             miti()
             print("miti")
        elif (negro.value()):
             mitad()
             print("mitad")                
        
