#!/usr/bin/env python
# -*- coding: utf-8 -*- 

""
Esse e um projeto feito pelo Python Works, simples libs para certas coisas
exemplo: criar um arquivo de error, dizer um error e etc, esse e um projeto 
para linux, o projeto do windows vai sair na versão 1.1

Para adicionar ao arquivo, digite import simplelibslinux, sim e bem grande.
"""

import os # Isso limpa a tela
from random import randint # Isso gera números random, obvius :O
from time import sleep # Importa uma lib que faz um time, prometo que farei algo igual para termos o nosso proprio :)

# Para os erros, tem essa lib

def classic_error(name):
	print("Error ocorred in program execution, type: "+ str(name)) # imprime a frase, e o error
	main1 = raw_input('Press Key to Continue...') # Isso continua o Programa
	exit()	# Isso fecha o programa

def classic_error_tick(mame):
	main2 = 1 # Isso e o main que mantem o while continuo ate o final da execução
	clock1 = 1 # Isso e o clock ou relogio que conta o tema
	while(main2<100):
		print("Um Error houve no seu programa, type: "+ str(mame)+ " Wait one seconds for close...") # Isso printa isso
		if(clock1<5):
			main2 = 101 # Termina o while
			print("Programa Terminado.") # Imprime isso
			exit() # Fecha o programa
		else:
			pass # Se não ele passa normalmente :)
		sleep(1) # Tempo para piscar
		os.system("clear") # Isso só funciona no linux.
		clock1 = clock1 + 1 #Isso adiciona ao clock + 1 
	
