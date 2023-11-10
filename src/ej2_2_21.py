def sumar_Lista_Numeros(lista: list):
    suma = 0
    for i in range(0, len(lista)):
        suma += lista[i]
    return suma


def crear_Str_Lista(lista: list):
    listaStr = ""
    for i in range(0, len(lista)):
        listaStr += str(lista[i])
        if i != len(lista) - 1:
            listaStr += " + "
    return listaStr

def comprobar_Numero(numero: str):
    try:
        if float(numero) < 0:
            return False
        else:
            return True
    except ValueError:
        return False

    

def main():
    listaNum = []
    print("El programa sumara todos los montos que introduzcas hasta que introduzcas el monto 0.")
    numero = "none"
    while numero != "0":
        numero = input("Introduce un monto: ")
        while comprobar_Numero(numero) != True:
            numero = input("Error. Introduce el monto otra vez: ")
        listaNum.append(float(numero))
    if sumar_Lista_Numeros(listaNum) > 1000:
        print(f"La suma de los montos: {crear_Str_Lista(listaNum)} = {sumar_Lista_Numeros(listaNum)}, dado que su compra supera los 1000€ se le aplicara un 10% de descuento lo que deja la cantidad a pagar en {sumar_Lista_Numeros(listaNum)*0.9:.2f}€.")
    else:
        print(f"La suma de los montos: {crear_Str_Lista(listaNum)} = {sumar_Lista_Numeros(listaNum):.2f}€.")
    

if __name__ == "__main__":
    main()  