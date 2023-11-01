def comprobar_Contraseña(intento: str, contraseña: str):
    if intento == contraseña:
        return True
    else:
        return False


def main():
    intento = input("Introduzca la contraseña: ")
    contraseña = "contraseña"
    while comprobar_Contraseña(intento, contraseña) != True:
        intento = input("Error, la contraseña no es correcta. Introduzca otra vez la contraseña: ")
    print("Contraseña correcta.")
    

if __name__ == "__main__":
    main()  