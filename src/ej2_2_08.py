def comprobar_Numero(numero: str):
    try:
        if int(numero) <= 0:
            return False
        else:
            return True
    except ValueError:
        return False


def crear_Triangulo(numero: int):
    trianguloStr = ""
    for i in range(1, numero + 1):
        if i % 2 != 0:
            for j in range (i, 0, -1):
                if j % 2 != 0:
                    trianguloStr += str(j)
                    if j != 1:
                        trianguloStr += " "
            if i != numero and i != numero - 1:
                trianguloStr += "\n"    
    return trianguloStr


def main():
    numero = input("Introduzca un número entero positivo: ")
    while comprobar_Numero(numero) != True:
        numero = int(input("Error. Introduzca un número entero positivo: "))
    numero = int(numero)
    print(crear_Triangulo(numero))


if __name__ == "__main__":
    main()  