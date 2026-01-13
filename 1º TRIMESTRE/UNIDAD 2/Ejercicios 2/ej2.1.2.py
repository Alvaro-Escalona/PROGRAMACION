#Escribir un programa que almacene la cadena de caracteres contraseña en una
# variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
# introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
# mayúsculas y minúsculas. 

contraseña = "EstofadoDeP4p4"

contraseña_usuario = str(input("Introduce una contraseña: "))

contraseña1 = contraseña.lower()
contraseña_usuario1 = contraseña_usuario.lower()

if contraseña_usuario1 == contraseña1:
    print ("Contraseña correcta")
else: 
    print ("Contraseña incorrecta")


