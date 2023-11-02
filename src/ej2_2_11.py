def devolver_Letra(palabra: str, posicion: int):
    return palabra[posicion]


def main():
    palabra = input("Introduzca una palabra: ")
    for i in range(len(palabra)-1, -1, -1):
        print(devolver_Letra(palabra, i))


if __name__ == "__main__":
    main()  