def calcular_Años(edad: int):
    años = ""
    for i in range(1, edad+1):
        años += str(i)
        if i != edad:
            años += "-"
        else:
            años += "."
    return años


def main():
    edad = int(input("Introduzca su edad en años: "))
    print(f"Esta es la cadena de todos los años que ha cumplido: \n{calcular_Años(edad)}")
    

if __name__ == "__main__":
    main()   