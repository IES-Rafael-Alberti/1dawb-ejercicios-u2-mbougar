"""Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar."""

def is_Par(num1:int):
    if num1 % 2 == 0:
        return True
    else:
        return False


def main():
    numero = int(input("Introduzca un número entero: "))
    if is_Par(numero) == True:
        print("El número introducido es par.")
    else:
        print("El número introducido es impar.")


if __name__ == "__main__":
    main()
