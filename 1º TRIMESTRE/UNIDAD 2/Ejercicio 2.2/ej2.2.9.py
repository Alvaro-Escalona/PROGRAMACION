#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta. 


def verificar_contraseña(a, b):
    if a.lower() != b.lower():
        return False
    else:
        return True
        
    
#  PROGRAMA PRINCIPAL

contraseña = input("Introduce la contraseña que quieras guardar: ")
contraseña2 =input("Introduce la contraseña para acceder: ")

while verificar_contraseña(contraseña, contraseña2) == False:
    if verificar_contraseña == False:
        contraseña = input("ERROR, intentalo de nuevo: ")
    else: 
        print ("Contraseña correcta: ")

    

 
    