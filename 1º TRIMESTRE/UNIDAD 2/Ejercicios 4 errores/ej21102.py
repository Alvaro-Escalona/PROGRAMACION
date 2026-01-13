import os

def menu_pizza():
    os.system("cls")
    print("Bienvenido a la pizzería Galileo Galilei")
    print("¿Qué tipo de pizza quieres?")
    print("1. Vegetariana")
    print("2. No vegetariana")
    print("0. TERMINAR PEDIDO")

def ingredientes_vegetarianos():
    print("Elige un ingrediente:")
    print("1. Pimiento")
    print("2. Tofu")
    print("0. VOLVER ATRÁS")

def ingredientes_no_vegetarianos():
    print("Elige un ingrediente:")
    print("1. Pepperoni")
    print("2. Jamón")
    print("3. Salmón")
    print("0. VOLVER ATRÁS")

# Programa principal

if __name__ == "__main__":
    comanda = []  # Lista para guardar las pizzas elegidas
    option = -1

    while option != 0:
        menu_pizza()

        try:
            option = int(input("Selecciona un tipo de pizza: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            input("Pulsa Enter para continuar...")
            continue

        match option:
            case 1:  # Vegetariana
                os.system("cls")
                ingredientes_vegetarianos()
                try:
                    ing_option = int(input("Selecciona un ingrediente: "))
                except ValueError:
                    print("Opción no válida.")
                    continue

                match ing_option:
                    case 1:
                        pizza = "Pizza vegetariana con pimiento"
                        print(f"Has añadido: {pizza}")
                        comanda.append(pizza)
                    case 2:
                        pizza = "Pizza vegetariana con tofu"
                        print(f"Has añadido: {pizza}")
                        comanda.append(pizza)
                    case 0:
                        continue
                    case _:
                        print("Opción no válida.")
            case 2:  # No vegetariana
                os.system("cls")
                ingredientes_no_vegetarianos()
                try:
                    ing_option = int(input("Selecciona un ingrediente: "))
                except ValueError:
                    print("Opción no válida.")
                    continue

                match ing_option:
                    case 1:
                        pizza = "Pizza no vegetariana con pepperoni"
                        print(f"Has añadido: {pizza}")
                        comanda.append(pizza)
                    case 2:
                        pizza = "Pizza no vegetariana con jamón"
                        print(f"Has añadido: {pizza}")
                        comanda.append(pizza)
                    case 3:
                        pizza = "Pizza no vegetariana con salmón"
                        print(f"Has añadido: {pizza}")
                        comanda.append(pizza)
                    case 0:
                        continue
                    case _:
                        print("Opción no válida.")
            case 0:
                os.system("cls")
                print("HAS TERMINADO SU PEDIDO. ¡GRACIAS!")
                if comanda:
                    print("Estas son las pizzas que has seleccionado:")
                    for i, pizza in enumerate(comanda, start=1):
                        print(f"{i}. {pizza}")
                else:
                    print("No has seleccionado ninguna pizza.")
                print("¡Hasta pronto!")
            case _:
                print("Opción no válida.")

        input("Pulsa Enter para continuar...")
