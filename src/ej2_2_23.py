def comprobar_Palabra(palabra: str):
    contador = 0
    for i in range(0, len(palabra)):
        if comprobar_Numero(palabra[i]) == True:
            contador += 1
    return contador


def comprobar_Numero(numero: str):
    try:
        if int(numero) < 0:
            return False
        else:
            return True
    except ValueError:
        return False


def main():
    loop = True
    lineas = 0
    contadorDigitos = 0
    while loop == True:
        libro = input("Libro: ")
        if libro == "*":
            print(f"Fin. Se leyeron {lineas} líneas completas")
            loop = False
        elif libro == "/":
            lineas += 1
            print(f"Línea completa. Aparecen {contadorDigitos} dígitos numéricos")
            contadorDigitos = 0
        else:
            contadorDigitos += comprobar_Palabra(libro)


if __name__ == "__main__":
    main()  