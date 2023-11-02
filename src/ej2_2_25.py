def encontrar_Mas_Larga(lista: list):
    mayor = ""
    for i in range(0, len(lista)):
        if len(lista[i]) > len(mayor):
            mayor = lista[i]
    return mayor
   

def main():
    print("El programa sumara todos los números enteros positivos que introduzcas hasta que introduzcas el número 0.")
    frase = input("Introduce una frase: ")
    listaPalabras = frase.split(" ")
    while len(listaPalabras) < 2:
        print("Para descubrir la palabra mas larga de una frase la frase debe contener al menos 2 palabras.")
        frase = input("Introduce una frase de al menos 2 palabras: ")
        listaPalabras = frase.split(" ")
    print(f"La frase introducida contiene {len(listaPalabras)} palabras, la palabra más larga es: {encontrar_Mas_Larga(listaPalabras)}.")    
    

if __name__ == "__main__":
    main()  