def comprobar_Primo(numero: int):
    contador = 0
    for i in range(1, int(numero/2) + 1):
        if numero % i == 0:
            contador += 1
            if contador > 1:
                return False
    return True    

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
        numero = int(input("Error. Introduzca un número entero positivo: "))
    numero = int(numero)
    if comprobar_Primo(numero) == True:
        print(f"El número {numero} es primo.")
    else: 
        print(f"El número {numero} NO es primo.")
    

if __name__ == "__main__":
    main()  