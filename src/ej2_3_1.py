def calcular_Años(edad: int):
    años = ""
    for i in range(1, edad+1):
        años += str(i)
        if i != edad:
            años += "-"
        else:
            años += "."
    return años


def comprobar_Numero(numero: str):
    try:
        if int(numero) < 1:
            return False
        else:
            return True
    except ValueError:
        return False


def main():
    edad = input("Introduzca su edad en años: ")
    while comprobar_Numero(edad) != True:
        edad = input("Introduzca su edad en años: ")
    print(f"Esta es la cadena de todos los años que ha cumplido: \n{calcular_Años(edad)}")
    

if __name__ == "__main__":
    main()   
