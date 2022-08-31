#Practica de laboratorio N°3 
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
    stop(tiempo)
    led1.value(0)
    stop(tiempo)
    led2.value(1)
    stop(tiempo)
    led2.value(0)
    stop(tiempo)
    led3.value(1)
    stop(tiempo)
    led3.value(0)
    stop(tiempo)
    led4.value(1)
    stop(tiempo)
    led4.value(0)
    stop(tiempo)
    led5.value(1)
    stop(tiempo)
    led5.value(0)
    stop(tiempo)
    led6.value(1)
    stop(tiempo)
    led6.value(0)
    stop(tiempo)
    led7.value(1)
    stop(tiempo)
    led7.value(0)
    stop(tiempo)
    led8.value(1)
    stop(tiempo)
    led8.value(0)
    stop(tiempo)

#alumbran leds pares    
def derechapares():
    led2.value(1)
    sleep(tiempo)
    led2.value(0)
    sleep(tiempo)
    led4.value(1)
    sleep(tiempo)
    led4.value(0)
    sleep(tiempo)
    led6.value(1)
    sleep(tiempo)
    led6.value(0)
    sleep(tiempo)
    led8.value(1)
    sleep(tiempo)
    led8.value(0)
    sleep(tiempo)

    
#Va hacia la izquierda  
def izquierda():
    led8.value(1)
    stop(tiempo)
    led8.value(0)
    stop(tiempo)
    led7.value(1)
    stop(tiempo)
    led7.value(0)
    stop(tiempo)
    led6.value(1)
    stop(tiempo)
    led6.value(0)
    stop(tiempo)
    led5.value(1)
    stop(tiempo)
    led5.value(0)
    stop(tiempo)
    led4.value(1)
    stop(tiempo)
    led4.value(0)
    stop(tiempo)
    led3.value(1)
    stop(tiempo)
    led3.value(0)
    stop(tiempo)
    led2.value(1)
    stop(tiempo)
    led2.value(0)
    stop(tiempo)
    led1.value(1)
    stop(tiempo)
    led1.value(0)
    stop(tiempo)    
 #alumbran leds pares    
def izquierdaimpares():
    led7.value(1)
    sleep(tiempo)
    led7.value(0)
    sleep(tiempo)
    led5.value(1)
    sleep(tiempo)
    led5.value(0)
    sleep(tiempo)
    led3.value(1)
    sleep(tiempo)
    led3.value(0)
    sleep(tiempo)
    led1.value(1)
    sleep(tiempo)
    led1.value(0)
    sleep(tiempo)
    
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
        #valor=amarillo.value()+azul.value()*2+verde.value()*4+negro.value()*8
        #print (valor)
        #if dato==2:
        stop(150)
        if (azul.value() and not amarillo.value() and not verde.value() and not negro.value()):
            print(f"izquierda tiempo: {tiempo}")
            izquierda()
        if (amarillo.value() and not azul.value() and not verde.value() and not negro.value()):
            derecha()
            print("derecha")    
        if (verde.value() and not azul.value() and not amarillo.value() and not negro.value()):
            derechapares()
            print("derecha pares")
        if (negro.value() and not verde.value() and not azul.value() and not amarillo.value()):
            izquierdaimpares()
            print("izquierda impares")
        if (rojo.value()):    
            tiempo=tiempo+35
            stop(120)
#2 botones                    
        if (amarillo.value() and verde.value() and not azul.value() and not negro.value()):
            derecha()
            miti()
            print("derecha y miti")
        if (amarillo.value() and azul.value()and not verde.value() and not negro.value()):
            todos()
            izquierda()
            print("todos e izquierda")
        if (amarillo.value() and negro.value()and not azul.value() and not verde.value()):
            unosi()
            izquierdaimpares()
            print("unosi e izquierdaimpares")
        if (azul.value() and verde.value()and not amarillo.value() and not negro.value()):
            derechapares()
            unosi()
            print("izquierda y derechapares")
        if (azul.value() and negro.value()and not verde.value() and not amarillo.value()):
            izquierda()
            izquierdaimpares()
            print("izquierda e izquierda impares")  
        if (verde.value() and negro.value()and not azul.value() and not amarillo.value()):
            derechapares()
            izquierdaimpares()
            print("derechapares y izquierdaimpares")
        if (verde.value() and amarillo.value()and not azul.value() and not negro.value()):
            ida()
            miti()
            print("ida y miti")
 #3 botones           
        if (azul.value() and amarillo.value() and negro.value() and not verde.value()):
            derecha()
            mitad()
        if (azul.value() and amarillo.value() and verde.value() and not negro.value()):
            todos()
            izquierda()
        if (azul.value() and negro.value() and verde.value() and not amarillo()):
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