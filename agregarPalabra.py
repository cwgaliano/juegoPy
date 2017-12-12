from menu import addMenu


def addWord(listWords):

    while True:
        addMenu()
        check=0
        word = input("Escriba palabra a agregar: ").lower()

        if listWords == [] :
            listWords.append(word)
            check = 1
            print()
            ("Palabra agregada con exito")
            print()
            
        else :
            for indicator in listWords:
                if indicator == word :
                    check = 1
                    print()
                    print("Palabra no agregada ya existe")
                    print()

        if check == 0 :
            listWords.append(word)
            print()
            print("Nueva palabra agregada con exito que es: " + word)
            print()
        

        if "si" == input("Desea terminar el ingreso de palabra (si) o (no) ") :
            break
    
    return listWords 
