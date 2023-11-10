def encontrar_Mayor_Lista(lista: list):
    mayor = 0
    for i in range(0, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor


def crear_Str_Lista(lista: list):
    listaStr = ""
    for i in range(0, len(lista)):
        listaStr += str(lista[i])
        if i != len(lista) - 1:
            listaStr += ", "
    return listaStr

def comprobar_Numero(numero: str):
    try:
        if int(numero) < 0:
            return False
        else:
            return True
    except ValueError:
        return False

    

def main():
    listaNum = []
    print("El programa te pedira números enteros positivos hasta que introduzcas el número 0.")
    loop = True
    while loop == True:
        numero = input("Introduce un número: ")
        while comprobar_Numero(numero) != True:
            numero = input("Error. Introduce el número otra vez: ")
        listaNum.append(int(numero))
        if numero == "0":
            loop = False
    print(f"Ha introducido los números: {crear_Str_Lista(listaNum)}. El mayor es: {encontrar_Mayor_Lista(listaNum)}.")
    

if __name__ == "__main__":
    main()  