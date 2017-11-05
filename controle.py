
import RPi.GPIO as GPIO
import time
#import sys

from espeak import espeak
from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event3')


#filtrando por botoes
#no codigo = 1 botao e gpio ligados
#no codigo = 0 carro parado e gpios desligadas
# gpio 16 eh pra esquerda / gpio 18 eh pra direita (frente ambas ligadas)
#gpio 22 eh pra tras
#codigo desliga a ponte H (trazeira) antes de ligar as gpios de frente para
#nao dar curto no motor quando inverter a ponte H 

aBtn = 114
bBtn =28
xBtn = 115
yBtn = 158
up = 163
down = 165
left = 208
right = 168
start = 164

def botoes():
         
       for event in gamepad.read_loop():
             
        if event.type == ecodes.EV_KEY:
         if event.value == 1:
            if event.code == yBtn:
                print("Y")
            elif event.code == bBtn:
                print("B")
            elif event.code == aBtn:
                print("A")
            elif event.code == xBtn:
                print("X")

            elif event.code == up:
                print("frente")
                GPIO.output(22, False)
                time.sleep (0.5)
                GPIO.output(16, True)
                GPIO.output(18, True)
                                                
            elif event.code == down:
                print("tras")
                GPIO.output(16, False)
                GPIO.output(18, False)
                time.sleep (0.5)
                GPIO.output(22, True)
            elif event.code == left:
                print("esquerda")
                GPIO.output(22, False)
                time.sleep (0.5)
                GPIO.output(16, True)
                GPIO.output(18, False)
            elif event.code == right:
                print("direita")
                GPIO.output(22, False)
                time.sleep (0.5)
                GPIO.output(16, False)
                GPIO.output(18, True)

            elif event.code == start:
                print("start")
         if event.value == 0:
            print ('parado')
            GPIO.output(16, False)
            GPIO.output(18, False)
            GPIO.output(22, False)
            break







