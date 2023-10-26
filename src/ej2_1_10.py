




def main():
    print("""Elige una opción de tipo de pizza:
    1. Vegetariana
    2. No vegetariana
""")
    opcion = input("Opción: ")
    while opcion != "1" and opcion != "2":
        opcion = input("Esa no es una opción posible, elige [1, 2]. Opción: ")
    if opcion == 1:
        pizzaTipo = 1
        print("""Elige un ingrediente:
    1. Pimiento
    2. Tofu
""")
        opcion = input("Opción: ")
        while opcion != "1" and opcion != "2":
            opcion = input("Esa no es una opción posible, elige [1, 2]. Opción: ")
        if opcion == 1:
            pizzaIngr = 11
        else:
            pizzaIngr = 12
    else:
        pizzaTipo = 2
        print("""Elige un ingrediente:
    1. Peperoni
    2. Salmón
    3. Jamón
""")
        opcion = input("Opción: ")
        while opcion != "1" and opcion != "2":
            opcion = input("Esa no es una opción posible, elige [1, 2]. Opción: ")
        if opcion == 1:
            pizzaIngr = 21
        elif opcion == 2:
            pizzaIngr = 22
        else:
            pizzaIngr = 23
    print(pizzaIngr)
    

if __name__ == "__main__":
    main()