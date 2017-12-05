#!/usr/bin/env python3

from menu import mainMenu
from jugar import game 
from saveLoads import *

listWords = load()

while True:
	
	mainMenu()
	option = int(input("Escriba numero de opcion: "))

	if option == 3 :
		break
	elif option == 2:
		print("hacer algo")
	elif option == 1:
		print("hacer lo otro")
	
	
save(listWords)
