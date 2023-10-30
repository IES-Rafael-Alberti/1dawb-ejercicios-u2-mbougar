def comprobar_Numero(numero: str, posTrue: bool):
    if posTrue == True and numero[0] == "-":
        return False
    elif posTrue == True and numero.isdecimal() == True:
        return True
    elif posTrue == False and numero[0] != "-":
        return False
    elif posTrue == False and numero.replace(numero[0],"").isdecimal() == True:
        return True
    else:
        return False
        

def cadena_Numeros(numero: int):
    numeroStr = ""
    for i in range(1, numero+1):
        if i % 2 != 0:
            numeroStr += str(i)
            if i != numero:
                numeroStr += ", "
            else:
                numeroStr += "."
    return numeroStr


def main():
    numero = input("Introduzca un número entero positivo: ")
    while comprobar_Numero(numero, True) != True or numero == "0":
        numero = input("Error. Introduzca un número entero positivo: ")
    numero = int(numero)
    print(f"Todos los números impares desde 1 hasta {numero} separados por comas son: {cadena_Numeros(numero)}")

if __name__ == "__main__":
    main()   