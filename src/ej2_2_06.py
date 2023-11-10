def crear_Triangulo(altura: int):
    trianguloStr = ""
    for i in range(1, altura + 1):
        trianguloStr += ("*" * i)
        if i != (altura):
            trianguloStr += "\n"
    return trianguloStr


def main():
    altura = int(input("Introduzca la altura del triangulo: "))
    print(crear_Triangulo(altura))


if __name__ == "__main__":
    main()  