"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""


def comprobar_Tipo(tipo: str):
    if tipo.lower() == "vegetariana" or tipo.lower() == "no vegetariana":
        return True
    else:
        return False


def comprobar_Ingrediente(tipo: str, ingrediente: int):
    if tipo.lower() == "vegetariana":
        if ingrediente == 1:
            return "pimiento"
        else:
            return "tofu"
    else:
        if ingrediente == 1:
            return "peperoni"
        elif ingrediente == 2:
            return "jamón"
        else:
            return "salmón"


def main():
    tipo = input("Introduzca el tipo de pizza que quiere (vegetariana o no vegetariana): ")
    while comprobar_Tipo(tipo) == False:
        tipo = input("Error. Introduzca el tipo de pizza que quiere (vegetariana o no vegetariana): ")
    if tipo.lower() == "vegetariana":
        print(f"Usted ha elegido una pizza {tipo.lower()}. Estos son los ingredientes.\n\n\t\t1. Pimiento.\n\t\t2. Tofu.\n\nSeleccione un ingrediente (1 o 2): ", end="")
        ingrediente = int(input())
        while ingrediente != 1 and ingrediente != 2:
            ingrediente = int(input("Error. Seleccione un ingrediente (1 o 2): "))
        print(f"La pizza que ha elegido es {tipo.lower()}, dicha pizza lleva mozzarella, tomate y {comprobar_Ingrediente(tipo, ingrediente)}.")
        print("Esperamos que disfrute su pizza!")
    else:
        print(f"Usted ha elegido una pizza {tipo.lower()}. Estos son los ingredientes.\n\n\t\t1. Peperoni.\n\t\t2. Jamón.\n\t\t3. Salmón.\n\nSeleccione un ingrediente (1, 2 o 3): ", end="")
        ingrediente = int(input())
        while ingrediente != 1 and ingrediente != 2 and ingrediente != 3:
            ingrediente = int(input("Error. Seleccione un ingrediente (1, 2 o 3): "))
        print(f"La pizza que ha elegido es {tipo.lower()}, dicha pizza lleva mozzarella, tomate y {comprobar_Ingrediente(tipo, ingrediente)}.")
        print("Esperamos que disfrute su pizza!")


if __name__ == "__main__":
    main()