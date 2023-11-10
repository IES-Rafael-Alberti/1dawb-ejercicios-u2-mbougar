def eco(palabra:str):
    if palabra == "salir":
        return False
    else:
        return True
    

def main():
    print("""El programa repetira todo lo que introduzca hasta que introduzca "salir":""", end="")
    palabra = input()
    while eco(palabra) == True:
        print(palabra)
        palabra = input()


if __name__ == "__main__":
    main()  