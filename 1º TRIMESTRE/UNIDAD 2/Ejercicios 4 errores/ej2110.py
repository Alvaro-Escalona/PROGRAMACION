# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los 
# ingredientes para cada tipo de pizza aparecen a continuación. 
# • Ingredientes vegetarianos: Pimiento y tofu. 
# • Ingredientes no vegetarianos: Pepperoni, Jamón y Salmón. 
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en 
# función de su respuesta le muestre un menú con los ingredientes disponibles para que 
# elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están 
# en todas las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es ¡ç
# vegetariana o no y todos los ingredientes que lleva.

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
    print("0. VOLVER ATRAS")

def ingredientes_no_vegetarianos():
    print("Elige un ingrediente:")
    print("1. Pepperoni")
    print("2. Jamón")
    print("3. Salmón")
    print("0. VOLVER ATRAS")

# Programa principal

if __name__=="__main__":

    os.system("cls")

    print("Bienvenido a la pizzería Galileo Galilei")
    comanda = []
    option = -1

    while option != 0:

        menu_pizza()
        option = int(input("Selecciona un tipo de pizza: "))
        
        match  option:
            case 1:
                os.system("cls")
                ingredientes_vegetarianos()
                ing_option = int(input("Selecciona un ingrediente: "))
                match ing_option:
                    case 1:
                        print("Has elegido una pizza vegetariana con mozzarella, tomate y pimiento.")
                        ingrediente="Pimiento"
                        comanda.append(ingrediente)
                        
                    case 2:
                        print("Has elegido una pizza vegetariana con mozzarella, tomate y tofu.")
                        ingrediente="Tofu"
                        comanda.append(ingrediente)
                    case 0:
                        menu_pizza()
                    case _:
                        print("Opción no válida.")
            case 2:
                os.system("cls")
                ingredientes_no_vegetarianos()
                ing_option = int(input("Selecciona un ingrediente: "))
                match ing_option:
                    case 1:
                        print("Has elegido una pizza con mozzarella, tomate y pepperoni.")
                        ingrediente="Pepperoni"
                        comanda.append(ingrediente)
                    case 2:
                        print("Has elegido una pizza con mozzarella, tomate y jamón.")
                        ingrediente="Jamon"
                        comanda.append(ingrediente)
                    case 3:
                        print("Has elegido una pizza con mozzarella, tomate y salmón.")
                        ingrediente="Salmón"
                        comanda.append(ingrediente)
                    case 0:
                        menu_pizza()
                    case _:
                        print("Opción no válida.")
            case 0:
                print("HAS TERMINADO SU PEDIDO. ¡GRACIAS!")
                if comanda:
                    print("Estas son las pizzas que has seleccionado:")
                    for i, ingrediente in enumerate(comanda, start=1):
                        print(f"{i}. {ingrediente}")
                else:
                    print("No has seleccionado ninguna pizza.")
                    print("Hasta pronto")
            case _:
                print("Opción no válida.")
