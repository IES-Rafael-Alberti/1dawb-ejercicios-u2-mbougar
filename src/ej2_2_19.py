def comprobar_Numero(numero: str):
    try:
        if int(numero) > 3 or int(numero) < 1:
            return False
        else:
            return True
    except ValueError:
        return False


def main():
    print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                    █
█ Bienvenido al programa de gestión ejercicios.                      █
█                                                                    █
█ Seleccione 1 para ejecutar el último ejercicio termiando.          █
█ Seleccione 2 para imrpimir el listado de ejercicios en desarrollo. █
█ Seleccione 3 para finalizar el programa.                           █
█                                                                    █
█                                                                    █
█ Recuerde que en cualquier momento puede seleccionar una opción.    █
█                                                                    █
█                                                                    █
█                                                                    █
█                                                                    █
█                                                                    █          
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█ 1. Comenzar programa █ 2. Imprimir listado █ 3. Finalizar programa █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
""")
    loop = True
    while loop == True:
        option = input("Seleccione una opción: ")
        while comprobar_Numero(option) != True:
            option = input("**Error** El valor que ha introducido no corresponde con ninguna opción. Por favor introduzca un valor valido (1, 2 o 3): ")
        if option == "1":
            print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                    █
█ Ha seleccionado la opción número 1.                                █
█                                                                    █
█ Ejecutando \DAW1B_ProgPython\src\ej2_2_19.py...                    █
█ Traceback (most recent call last):                                 █
█       main()                                                       █
█   File "\DAW1B_ProgPython\src\ej2_2_18.py", line 8, in main        █
█       while numero != "-1":                                        █
█ UnboundLocalError: cannot access local variable 'numero' where it  █
█ is not associated with a value                                     █
█                                                                    █
█                                                                    █
█ Se ha detectado un error, por favor seleccione otra opción.        █
█                                                                    █                  
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█ 1. Comenzar programa █ 2. Imprimir listado █ 3. Finalizar programa █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
""")
        elif option == "2":
            print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                    █
█ Ha seleccionado la opción número 2.                                █
█                                                                    █
█ Mostrando listado de programas en desarrollo...                    █
█ [...]                                                              █
█ ej2_2_18 - *terminado*                                             █
█ ej2_2_19 - *en proceso*                                            █
█ ej2_2_20 - *en proceso*                                            █
█ ej2_2_21 - *en proceso*                                            █
█                                                                    █
█ Programas en estado *en proceso*: [27]                             █
█ Programas en estado *terminado*:  [03]                             █
█ Tiempo restante para la entrega: 3 horas y 27 minutos.             █                  
█                                                                    █
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█ 1. Comenzar programa █ 2. Imprimir listado █ 3. Finalizar programa █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
""")
        else:
            print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                    █
█ Ha seleccionado la opción número 3.                                █
█                                                                    █
█ Cerrando el programa...                                            █
█                                                                    █
█                                                                    █
█                                                                    █
█                                                                    █
█                                                                    █
█                                                                    █
█                                                                    █
█                                                                    █
█                                                                    █                  
█                                                                    █
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█ 1. Comenzar programa █ 2. Imprimir listado █ 3. Finalizar programa █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
""")
            loop = False
    
    
if __name__ == "__main__":
    main()  