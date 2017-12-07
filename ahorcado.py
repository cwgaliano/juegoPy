#!/usr/bin/env python3

from menu import mainMenu
from juego import game 
from saveLoads import *
from agregarPalabra import addWord

listWords = load()

while True:
	
	mainMenu()
	option = int(input("Escriba numero de opcion: "))

	if option == 3 :
		break
	elif option == 2:
		listWords = addWord(listWords)
	elif option == 1:
		game(listWords)
	
	
save(listWords)
