#Escribir un programa que pregunte por consola el precio de un producto en euros con dos
# decimales y muestre por pantalla el número de euros y el número de céntimos del precio
# introducido. 

precio = float(input("Introduce el precio del producto: "))
precio2= str(precio)
n = precio2.split (".")
euro = n [0]
centimos = n [1]
print ("El precio del producto es {} euros con {} centimos".format (euro , centimos) )