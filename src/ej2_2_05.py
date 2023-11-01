def calcular_Capital(amount: float, interest: float):
    amount *= 1 + interest / 100
    return amount


def main():
    amount = float(input("Introduzca una cantidad a invertir: "))
    startingtAmount = amount
    interest = float(input("Introduzca el porcentaje de interés anual de la inversión: "))
    years = int(input("Introduzca el número de años que mantendra la inversión: "))
    for i in range(1, years + 1):
        if i != 1:
            amount = calcular_Capital(amount, interest)
            print(f"Su inversión inicial fue: {startingtAmount:0.2f}€. Despues de {i} años su inversión estará valorada en: {amount:0.2f}€")
        else:
            amount = calcular_Capital(amount, interest) 
            print(f"Su inversión inicial fue: {startingtAmount:0.2f}€. Despues de {i} año su inversión estará valorada en: {amount:0.2f}€")

if __name__ == "__main__":
    main()  