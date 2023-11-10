def comprobar_Letra_Veces(palabra: str, letra: str):
    contador = 0
    for i in range(0, len(palabra)):
        if palabra[i] == letra:
            contador += 1
    return contador
    

def main():
    palabra = input("Introduzca una palabra: ")
    letra = input("Introduzca una letra: ")
    if comprobar_Letra_Veces(palabra, letra) == 1:
        print(f"La letra {letra} se repite {comprobar_Letra_Veces(palabra, letra)} vez.")
    else:
        print(f"La letra {letra} se repite {comprobar_Letra_Veces(palabra, letra)} veces.")


if __name__ == "__main__":
    main()  