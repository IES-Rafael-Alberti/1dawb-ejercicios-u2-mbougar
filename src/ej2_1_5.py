"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""


def comprobar_Edad(edad: int, edadMin:int):
    if edad > edadMin:
        return True
    else:
        return False
    

def comprobar_Ingresos(ingreso: int, ingresoMin:int):
    if ingreso > ingresoMin:
        return True
    else:
        return False


def comprobar_Tributa(edad:int, ingreso: int):
    if comprobar_Edad(edad, 16) == True and comprobar_Ingresos(ingreso, 1000) == True:
        return True
    else:
        return False


def main():
    edad = int(input("Introduzca su edad: "))
    ingresos = float(input("Introduzca sus ingresos mensuales: "))
    if comprobar_Tributa(edad, ingresos) == True:
        print("El usuario tiene que tributar.")
    else:
        print("El usuario NO tiene que tributar.")
    

if __name__ == "__main__":
    main()