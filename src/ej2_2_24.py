def comprobar_Numero(numero: str):
    try:
        if int(numero) < 0:
            return False
        else:
            return True
    except ValueError:
        return False
    

def comprobar_Primo(numero: int):
    contador = 0
    for i in range(1, int(numero/2) + 1):
        if numero % i == 0:
            contador += 1
            if contador > 1:
                return False
    return True 


def main():
    loop = True
    contador = 0
    while loop == True:
        numero = input("Introduzca un número entero positivo: ")
        while comprobar_Numero(numero) != True:
            numero = input("Error. Introduce el número otra vez: ")
        if numero != "0":
            if comprobar_Primo(int(numero)) == True:
                contador += 1   
        else:
            loop = False
    if contador == 1:
        print(f"En total se ha leído {1} número primo.")
    else:
        print(f"En total se han leído {contador} números primos.")       
    

if __name__ == "__main__":
    main()  