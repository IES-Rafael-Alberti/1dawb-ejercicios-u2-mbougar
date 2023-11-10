def sumar_Digitos_Numero(numero: str):
    suma = 0
    for i in range(0, len(numero)):
        suma += int(numero[i])
    return suma


def crear_Str_Numero(numero: str):
    numeroStr =""
    for i in range(0, len(numero)):
        numeroStr += str(numero[i])
        if i != len(numero) - 1:
            numeroStr += " + "
    return numeroStr

def comprobar_Numero(numero: str):
    try:
        if int(numero) <= 0:
            return False
        else:
            return True
    except ValueError:
        return False


def main():
    numero = input("Introduzca un número entero positivo: ")
    while comprobar_Numero(numero) != True:
        numero = input("Error. Introduce el número otra vez: ")
    print(f"{crear_Str_Numero(numero)} = {sumar_Digitos_Numero(numero)}.")
    

if __name__ == "__main__":
    main()  