"""
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
"""


def asignar_Precio(edad: int):
    if edad <= 4:
        precio = 0
        return precio
    elif edad < 18:
        precio = 5
        return precio
    else:
        precio = 10
        return precio


def comprobar_Edad(edad: int, edadMin:int):
    if edad > edadMin:
        return True
    else:
        return False


def main():
    edad = int(input("Introduzca su edad: "))
    while comprobar_Edad(edad, 0) == False:
        edad = int(input("Error. Introduzca su edad: "))
    if edad == 1:
        años = "año"
    else:
        años = "años"
    print(f"Tienes {edad} {años}, por tanto el precio de tu entrada es de {asignar_Precio(edad)}€.")



if __name__ == "__main__":
    main()