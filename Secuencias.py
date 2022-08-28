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
azul=pin(5,pin.IN)
negro=pin(18,pin.IN)
rojo=pin(19,pin.IN)
para=0.04
#------------------------------------------------------------------------
posipines=[13,12,14,27,26,25,33,32]
luces=[]
for i in posipines:
    luces.append  (pin(i,pin.OUT))
   # print(luces)
def derecha():   
    for i in luces:
        for j in range (2):
            i.value(not i.value())
            para(150)   
def izquierda():
    for i in reversed (luces):
        for j in range (2):
            i.value(not i.value())
            para(150)
while (True):
    if (amarillo.value()):
        derecha()
        print("si sirvio derecha")
    if (verde.value()):
        izquierda()
        print("si sirvio izquierda")   
        
#-----------------------------------------------------------------------
def derechapares():
    led2.value(1)
    sleep(para)
    led2.value(0)
    sleep(para)
    led4.value(1)
    sleep(para)
    led4.value(0)
    sleep(para)
    led6.value(1)
    sleep(para)
    led6.value(0)
    sleep(para)
    led8.value(1)
    sleep(para)
    led8.value(0)
    sleep(para)
#secuencia 2 boton verde
def izquierdaimpares():
    led1.value(1)
    sleep(para)
    led1.value(0)
    sleep(para)
    sleep(para)
    led3.value(1)
    sleep(para)
    led3.value(0)
    sleep(para)
    led5.value(1)
    sleep(para)
    led5.value(0)
    sleep(para)
    led7.value(1)
    sleep(para)
    led7.value(0)
while (True):
    if (amarillo.value()):
        derechapares()
        print("si sirviopares")
        
    