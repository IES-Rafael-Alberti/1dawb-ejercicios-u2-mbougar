"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""


def comprobar_Sexo(sexo: str):
    if sexo.lower() == "masculino":
        return sexo.lower()
    elif sexo.lower() == "femenino":
        return sexo.lower()
    else:
        return "Error"


def comprobar_Nombre(nombre: str):
    abecedario = "abcdefghijklmnñopqrtsuvwxyz"
    return abecedario.find(nombre[0].lower())


def main():
    sexo = input("Introduzca su sexo (masculino o femenino): ")
    nombre = input("Introduzca su nombre: ")
    while comprobar_Sexo(sexo) == "Error":
        sexo = input("Error. Introduzca su sexo (masculino o femenino): ")
    if comprobar_Sexo(sexo) == "masculino" and comprobar_Nombre(nombre) > 13:
        print("Su grupo correspondiente es el A")
    elif comprobar_Sexo(sexo) == "femenino" and comprobar_Nombre(nombre) < 12:
        print("Su grupo correspondiente es el A")
    else:
        print("Su grupo correspondiente es el B")

   
if __name__ == "__main__":
    main()