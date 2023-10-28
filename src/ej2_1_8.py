

def calcular_Rendimiento(puntuacion: float):
    if puntuacion == 0.0:
        rendimiento = "Inaceptable"
        beneficios = 2400 * puntuacion
        return rendimiento, beneficios
    elif puntuacion == 0.4:
        rendimiento = "Aceptable"
        beneficios = 2400 * puntuacion
        return rendimiento, beneficios
    else:
        rendimiento = "Meritorio"
        beneficios = 2400 * puntuacion
        return rendimiento, beneficios
    

def comprobar_Puntuacion(puntuacion: float):
    if puntuacion == 0.0:
        return True
    elif puntuacion == 0.4:
        return True
    elif puntuacion >= 0.6 and puntuacion <= 1.0:
        return True
    else:
        return False


def main():
    puntuacion = float(input("Introduzca su puntuación: "))
    while comprobar_Puntuacion(puntuacion) == False:
        puntuacion = float(input("Error. Introduzca su puntuación: "))
    rendimiento, beneficios = calcular_Rendimiento(puntuacion)
    print(f"Su nivel de rendimiento es {rendimiento.lower()}, dicho rendimiento le otorga un beneficio de {beneficios}€.")



if __name__ == "__main__":
    main()