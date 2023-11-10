def comprobar_Letra(palabra: str, letra: str, posicion: int):
    if palabra[posicion] == letra:
        return True
    else:
        return False
    

def main():
    palabra = input("Introduzca una palabra: ")
    letra = input("Introduzca una letra: ")
    contador = 0
    loop = True
    while loop == True and contador != len(palabra):
        if comprobar_Letra(palabra, letra, contador) == False:
            print(f"La letra {letra} no está en la posición {contador}.")
        else:
            print(f"La letra {letra} está en la posición {contador}.")
            loop = False
        contador += 1
    

if __name__ == "__main__":
    main()  