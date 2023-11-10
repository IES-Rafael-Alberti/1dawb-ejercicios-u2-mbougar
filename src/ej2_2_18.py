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
        if int(numero) < -1:
            return False
        else:
            return True
    except ValueError:
        return False


def main():
    loop = True
    listaPares = []
    while loop == True:
        numero = input("Introduzca un número entero positivo: ")
        while comprobar_Numero(numero) != True:
            numero = input("Error. Introduce el número otra vez: ")
        if numero != "-1":
            print(f"{crear_Str_Numero(numero)} = {sumar_Digitos_Numero(numero)}.")
            if int(numero) % 2 == 0:
                listaPares.append(numero)
        else:
            loop = False
    if len(listaPares) == 1:
        print(f"{1} de los números introducidos es par. {listaPares[0]} es par.")
    else:
        print(f"{len(listaPares)} de los números introducidos son pares.", end=" ")
        for i in range(0, len(listaPares)):
            print(listaPares[i], end="")
            if i != len(listaPares)-1 and i != len(listaPares)-2:
                print(", ", end="")
            elif i != len(listaPares)-1:
                print(" y ", end="")
            else:
                print(" son pares.")
        
    

if __name__ == "__main__":
    main()  