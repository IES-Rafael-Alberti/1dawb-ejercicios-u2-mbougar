def repetir_Palabra(palabra: str, veces: int):
    nuevaPalabra = ""
    for i in range(0,veces):
        nuevaPalabra += palabra
        if i != veces-1:
            nuevaPalabra += " "
    return nuevaPalabra


def main():
    palabra = input("Introduzca una palabra: ")
    print(repetir_Palabra(palabra, 10))
    


if __name__ == "__main__":
    main()   
