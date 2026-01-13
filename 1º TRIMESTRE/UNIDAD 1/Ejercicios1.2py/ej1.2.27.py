# Escribir un programa que pregunte el nombre el un producto, su precio y un número de
# unidades y muestre por pantalla una cadena con el nombre del producto seguido de su
# precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos
# y el coste total con 8 dígitos enteros y 2 decimales. 
producto= str(input("Introduce el producto: "))
precio = int(input("Introduce el  precio del producto: "))
unidades = int(input("Introduce el numero de unidades del producto: "))
suma= precio*unidades

print("Ha comprado {:03d} unidades de {} con un valor cada uno de {:06.2f} que es un total de {:08.2f} ".format (unidades, producto, precio, suma))