#PRÁCTICA DE LABORATORIO N°3
from machine import Pin as pin
from utime import sleep, sleep_ms as stop,sleep_us as pausar
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
tiempo=150
para=0.05
pausa=0.40
luces=[led1,led2,led3,led4,led5,led6,led7,led8]

def ida():
    for i in luces:
        for j in range (2):
            i.value(not i.value())
            stop(80)   
def vuelta():
    for i in reversed (luces):
        for j in range (2):
            i.value(not i.value())
            stop(80)
            
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
    
def print_led(a,b,c,d,e,f,g,h):
        led1.value(a) 
        led2.value(b)
        led3.value(c)
        led4.value(d)
        led5.value(e)
        led6.value(f)
        led7.value(g)
        led8.value(h)
        stop(150)
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
while True:
#solo boton
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
        if (rojo.value()):    
            for i in luces:
                for j in range (2):
                    i.value(not i.value())
                    para(tiempo)
                    t=tiempo+0.35
#2 botones                    
        if (amarillo.value() and verde.value()):
            derecha()
            miti()
            print("derecha y miti")
        if (amarillo.value() and azul.value()):
            todos()
            izquierda()
            print("todos e izquierda")
        if (amarillo.value() and negro.value()):
            unosi()
            izquierdaimpares()
            print("unosi e izquierdaimpares")
        if (azul.value() and verde.value()):
            derechapares()
            unosi()
            print("izquierda y derechapares")
        if (azul.value() and negro.value()):
            izquierda()
            izquierdaimpares()
            print("izquierda e izquierda impares")  
        if (verde.value() and negro.value()):
            derechapares()
            izquierdaimpares()
            print("derechapares y izquierdaimpares")
        if (verde.value() and amarillo.value()):
            ida()
            miti()
            print("ida y miti")
 #3 botones           
        if (azul.value() and amarillo.value() and negro.value()):
            derecha()
            mitad()
        if (azul.value() and amarillo.value() and verde.value()):
            todos()
            izquierda()
        if (azul.value() and negro.value() and verde.value()):
            derechapares()
            izquierdaimpares()    
        if (verde.value() and amarillo.value() and negro.value()):
            miti()
            mitad()
 #4 botones
        if (verde.value() and amarillo.value() and negro.value() and azul()):
            ida()
            vuelta()
            ida()
            todos()
                