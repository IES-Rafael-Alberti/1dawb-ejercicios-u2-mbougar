#no he importado la funcion comprobar_numero del ejercicio 2_2_03 porque si la importaba sin el "src." pytest no la reconocia, pero si la importaba con el "src." era python el que no la reconocia.


def comprobar_Numero(numero: str):
    try:
        if int(numero) <= 0:
            return False
        else:
            return True
    except ValueError:
        return False    


def cadena_Numeros(numero: int):
    numeroStr = ""
    for i in range(numero, -1, -1):
        numeroStr += str(i)
        if i != 0:
            numeroStr += ", "
    numeroStr += "."
    return numeroStr


def main():
    numero = input("Introduzca un número entero positivo: ")
    while comprobar_Numero(numero) != True:
        numero = input("Error. Introduzca un número entero positivo: ")
    numero = int(numero)
    print(f"La cuenta atrás desde {numero} hasta cero separados por comas es: {cadena_Numeros(numero)}")

if __name__ == "__main__":
    main()   