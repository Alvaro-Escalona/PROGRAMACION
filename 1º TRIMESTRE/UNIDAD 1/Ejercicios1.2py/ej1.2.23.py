#Escribir un programa que pregunte el correo electrónico del usuario en la consola y
# muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la
# arroba @) pero con dominio ceu.es. 

correo=str(input("Introduce el correo electronico: "))
p = correo.split("@")
correo2 = p[0] + ("@ceu.es")
print (correo2)