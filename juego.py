from menu import gameMenu
import random

def game(listWords):
    
    while True:
        
        gameMenu()
        
        
        guessWord = random.choice(listWords)
        guess = []
        print(guessWord)
    
        for indicator in range(len(guessWord)):
            print(indicator)
            
            while True :
                
                
               
                
            
                input()
        
        
        
        
        
        
        
        
        
        input()
        
        
        if "no" == input("Quiere jugar otra vez (no) o (si)"):
            break
        
