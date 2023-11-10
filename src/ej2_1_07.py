

def comprobar_Renta(renta: float):
    if renta < 10000:
        return 5
    if renta < 20000:
        return 15
    if renta < 35000:
        return 20
    if renta < 60000:
        return 30
    else:
        return 45


def main():
    renta = int(input("Introduzca su renta anual en euros: "))
    print(f"Su renta anual es de {renta}€, por lo tanto su tipo impositivo es del {comprobar_Renta(renta)}%.")
    

if __name__ == "__main__":
    main()
