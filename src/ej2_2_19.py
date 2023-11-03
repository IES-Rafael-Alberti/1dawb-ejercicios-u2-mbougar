import os


def borrar_Consola():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def comprobar_Numero(numero: str):
    try:
        if int(numero) > 3 or int(numero) < 1:
            return False
        else:
            return True
    except ValueError:
        return False
    

def comprobar_Numero_Nota(numero: str):
    try:
        if float(numero) < 0 or int(numero) > 10:
            return False
        else:
            return True
    except ValueError:
        return False


def main():
    listaNotas = []
    loop = True
    borrar_Consola()
    print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                      █
█ Bienvenido al programa de visualización de notas.                    █
█                                                                      █
█ Seleccione 1 para introducir una nota.                               █
█ Seleccione 2 para imrpimir el listado de notas.                      █
█ Seleccione 3 para finalizar el programa.                             █
█                                                                      █
█                                                                      █
█ Recuerde que en cualquier momento puede seleccionar una opción.      █
█                                                                      █
█                                                                      █
█                                                                      █
█                                                                      █
█                                                                      █          
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█ 1. Introduzca una nota █ 2. Imprimir listado █ 3. Finalizar programa █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
""")
    while loop == True:
        option = input("Seleccione una opción: ")
        while comprobar_Numero(option) != True:
            option = input("**Error** El valor que ha introducido no corresponde con ninguna opción. Por favor introduzca un valor valido (1, 2 o 3): ")
        if option == "1":
            borrar_Consola()
            print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                      █
█ Ha seleccionado introducir una nota.                                 █
█                                                                      █
█ Por favor, introduzca una nota                                       █
█                                                                      █          
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█ 1. Introduzca una nota █ 2. Imprimir listado █ 3. Finalizar programa █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
""")
            nota = float(input("Introduzca una nota: "))
            while comprobar_Numero_Nota(nota) != True:
                nota = float(input("Error. Introduzca una nota: "))
            listaNotas.append(nota)
        elif option == "2":
            borrar_Consola()
            print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                      █
█ Ha seleccionado imprimir listado.                                    █
█                                                                      █
█ Estas son las notas que ha introducido:                              █
█                                                                      █""")
            for i in range(0, len(listaNotas)):
                print("█ {:5.2f}                                                                █".format(listaNotas[i]))
            print("""█                                                                      █          
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█ 1. Introduzca una nota █ 2. Imprimir listado █ 3. Finalizar programa █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
""")
        else:
            borrar_Consola()
            print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                      █
█ Ha seleccionado finalizar programa.                                  █
█                                                                      █
█ Cerrando el programa...                                              █
█                                                                      █          
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█ 1. Introduzca una nota █ 2. Imprimir listado █ 3. Finalizar programa █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
""")
            loop = False
    
    
if __name__ == "__main__":
    main()  