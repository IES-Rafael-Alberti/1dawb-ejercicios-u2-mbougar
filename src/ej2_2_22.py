def sumar_Digitos_Numero(numero: str):
    suma = 0
    for i in range(0, len(numero)):
        if int(numero[i]) % 2 == 0:
            suma += 1
    return suma


def comprobar_Numero(numero: str):
    try:
        if int(numero) < 0:
            return False
        else:
            return True
    except ValueError:
        return False


def main():
    loop = True
    contador = 0
    while loop == True:
        numero = input("Introduzca un número entero positivo: ")
        while comprobar_Numero(numero) != True:
            numero = input("Error. Introduce el número otra vez: ")
        if numero != "0":
            if sumar_Digitos_Numero(numero) == 1:
                print(f"El número {numero} tiene {1} dígito entero.")
            else:
                print(f"El número {numero} tiene {sumar_Digitos_Numero(numero)} dígitos enteros.")
            contador += sumar_Digitos_Numero(numero)   
        else:
            loop = False
    if contador == 1:
        print(f"En total se ha leído {1} número par")
    else:
        print(f"En total se han leído {contador} números pares")       
    

if __name__ == "__main__":
    main()  