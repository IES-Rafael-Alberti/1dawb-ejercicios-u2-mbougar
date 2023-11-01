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
    for i in range(1, numero+1):
        if i % 2 != 0:
            numeroStr += str(i)
            if i != numero and i != numero-1:
                numeroStr += ", "
    numeroStr += "."
    return numeroStr


def main():
    numero = input("Introduzca un número entero positivo: ")
    while comprobar_Numero(numero) != True:
        numero = input("Error. Introduzca un número entero positivo: ")
    numero = int(numero)
    print(f"Todos los números impares desde 1 hasta {numero} separados por comas son: {cadena_Numeros(numero)}")

if __name__ == "__main__":
    main()   
