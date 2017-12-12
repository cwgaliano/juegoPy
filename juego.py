from menu import gameMenu
import random
from menu import winner
from menu import loser
from menu import menuHanged

def game(listWords):
    
    while True:
        
        gameMenu()
        
        life = 6
        guessWord = random.choice(listWords)
        guess = []
        word = []
        print(guessWord)
    
        for indicator in range(len(guessWord)):
            word.append("_")
            guess.append(guessWord[indicator])

        print (word) 
        
        word.pop(0)
        word.insert(0, guess[0])
        
        while True:
            
            
            menuHanged()
            
            print("Palabra a adivinar es: " + str(word))
            checkword = 0
            letter = input("Ingrese letra: ").lower()
        
            for indicator in range(len(guess)):
                
                if letter == guess[indicator]:
                    word.pop(indicator)
                    word.insert(indicator, letter)
                    checkword = 1
                    
                    print(word)
                    print(guess)
                    input()
                
                    if word == guess:
                        winner()
                        print("Has ganado")
                        break
                
                
            if checkword == 0 :
                life = life - 1
                
            if life == 0 :
                loser()
                print("GAME OVER" )
                break
                
            
            if letter == "si":
                break
                
        
        
        if "no" == input("Quiere jugar otra vez (no) o (si)"):
            break
        
