def crear_Tabla(longitud: int):
    tablaStr = ""
    for i in range(1, longitud + 1):
        tablaStr += str(i) + " x 10 = " + str(i * 10)
        if i != (longitud):
            tablaStr += "\n"
    return tablaStr


def main():
    longitud = 10
    print("La tabla de multiplicar del 10 es: ")
    print(crear_Tabla(longitud))


if __name__ == "__main__":
    main()  