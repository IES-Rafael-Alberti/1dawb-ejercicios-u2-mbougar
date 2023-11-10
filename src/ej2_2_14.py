def sumar_Lista_Numeros(lista: list):
    suma = 0
    for i in range(0, len(lista)):
        suma += lista[i]
    return suma


def crear_Str_Lista(lista: list):
    listaStr = ""
    for i in range(0, len(lista)):
        listaStr += str(lista[i])
        if i != len(lista) - 1:
            listaStr += " + "
    return listaStr

def comprobar_Numero(numero: str):
    try:
        int(numero)
        return True
    except ValueError:
        return False

    

def main():
    listaNum = []
    print("El programa sumara todos los números enteros positivos que introduzcas hasta que introduzcas el número 0.")
    numero = "none"
    while numero != "0":
        numero = input("Introduce un número: ")
        while comprobar_Numero(numero) != True:
            numero = input("Error. Introduce el número otra vez: ")
        listaNum.append(int(numero))
    print(f"{crear_Str_Lista(listaNum)} = {sumar_Lista_Numeros(listaNum)}.")
    

if __name__ == "__main__":
    main()  