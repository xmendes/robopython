# -*- coding: utf-8 -*-
#carro controle RAFAEL MENDES
#usando as Gpios e desligando avisos
#usando a gpio por BOARD = numeros fisicos de localização dos pinos
#usando time para dar tempo para os acionamentos de gpio.

import RPi.GPIO as GPIO
import time
#import sys

from espeak import espeak
from evdev import InputDevice, categorize, ecodes

import sensorultrasonico
import controle

GPIO.setwarnings(False)

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


#evdev pra ler os botoes do gamepad bluetooth

from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event3')

#codigo dos botoes 
aBtn = 114
bBtn =28
xBtn = 115
yBtn = 158

up = 163
down = 165
left = 208
right = 168

start = 164





#imprime o nome do gamepad pra ver se esta conectado
print(gamepad)

try: 

 while True:
       distance = sensorultrasonico.sensor()

       controle.botoes()
       
       print ('fim do loop')


except KeyboardInterrupt:
 
  GPIO.cleanup()       




    
