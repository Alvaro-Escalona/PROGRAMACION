#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
# ingredientes para cada tipo de pizza aparecen a continuación.
# 
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Pepperoni, Jamón y Salmón.
# 
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
# función de su respuesta le muestre un menú con los ingredientes disponibles para que
# elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están
# en todas las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es
# vegetariana o no y todos los ingredientes que lleva. 

n = input("¿Quieres una pizza vegetariana? (si/no): ")
if n=="si":
    print("Los ingredientes disponibles son: Pimiento y Tofu")
    ingrediente = input("Elige un ingrediente: ")
    print("Has elegido una pizza vegetariana con mozzarella, tomate y {}".format(ingrediente))
else:
    print("Los ingredientes disponibles son: Pepperoni, Jamón y Salmón")
    ingrediente = input("Elige un ingrediente: ")
    print("Has elegido una pizza no vegetariana con mozzarella, tomate y {}".format(ingrediente))
       