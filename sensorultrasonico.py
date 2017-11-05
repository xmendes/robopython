
# -*- coding: latin_1 -*-

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)

def sensor():  
   
        print "Sensor ultrassonico"
        
        GPIO.setmode(GPIO.BOARD)

        GPIO_Gatilho = 24
        GPIO_Eco    = 26
         
        # Seta os pinos como saida e entrada respectivamente
        GPIO.setup(24,GPIO.OUT)
        GPIO.setup(26,GPIO.IN)
             
         
        # Seta o pino do gatilho como desligado
        GPIO.output(GPIO_Gatilho, False)
         
        # Aguarda 10 segundos para instrução
        time.sleep(1)
     
        # envia um pulso de 10us no gatilho
        GPIO.output(GPIO_Gatilho, True)
        time.sleep(0.00001)
        #desativa o gatilho
        GPIO.output(GPIO_Gatilho, False)
        #inicia a contagem de tempo
        inicio = time.time()
     
        # enquanto o eco nao receber pulso o tempo continua
        while GPIO.input(GPIO_Eco)==0:
          inicio = time.time()
     
        # quando o eco receber o pulso cria e setado 1 variavel para calcular
        #o tempo que recebeu
        while GPIO.input(GPIO_Eco)==1:
          tempo_parado = time.time()
     
        # Calcula o pulso
        transcorrido = tempo_parado - inicio
     
        # multiplica o tempo transcorrido pela velocidade do som (34000 cm/s)
        distancia_total = transcorrido * 34000
     
        # That was the distance there and back so halve the value
        distancia_total = distancia_total / 2
     
        # formata a variavel distancia como decimal de 1 casa
         
        print "A distancia : %.1f" % distancia_total
        


        #  parte do espeak (ignore caso não queira usar)-------------------------
        #converte float em string
        distancia = str("%.1f" %distancia_total)
        # substitue ponto por virgula
        if distancia_total <= 10:
           #distancia = distancia.replace(".",",")
           espeakfala ="OBJETO PROXIMO, POR FAVOR RETIRE O OBJETO OU VOLTE PARA TRAZ. A distancia e de ", distancia ," centimetros"
           os.system('espeak -vpt -s 150 "{0}"'.format(espeakfala))


