#Escribe un programa que pida el importe final de un artículo y calcule e imprima porpantalla el IVA que se ha pagado
# y el importe sin IVA (suponiendo que se ha aplicado untipo de IVA del 10%). 
producto = int(input("Introduzca el precio del producto: "))
iva = 1.1
r = producto * iva
iva2 = r - producto
print ("El precio del producto original es", producto, "€ y el precio final del producto es", r, "€ con un 10% de IVA que equivale a un" ,iva2 ,"€ mas"  )