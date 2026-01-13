producto = float(input("Introduce el precio del producto: "))
iva = float(input("Introduce el porcentaje de IVA: "))
iva2 =  (((iva / 100) +1) * producto) - producto
r = ((iva2 / 100) +1) * producto

print ("El precio final del producto con IVA es:", r,"€ con una suma de", iva2,"€ de IVA")
