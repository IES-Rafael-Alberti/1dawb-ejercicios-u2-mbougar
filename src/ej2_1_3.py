def division(dividendo, divisor):
    if divisor == 0:
        return "Error"
    else:
        return str(dividendo/divisor)


def main():
    dividendo = float(input("Introduce un dividendo: "))
    divisor = float(input("Introduce un divisor: "))
    print(division(dividendo, divisor))


if __name__ == "__main__":
    main()