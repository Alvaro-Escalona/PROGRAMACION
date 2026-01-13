# Escribir un programa que pida al usuario que introduzca una frase en la consola y una
# vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en
# mayúscula. 

frase= str(input("Introduce una frase: "))
vocal= str(input("Introduce una vocal: "))

if vocal == 'a' and 'A':
    print (frase.replace(vocal,vocal.upper()))
elif vocal == 'e' or 'E':
    print (frase.replace(vocal,vocal.upper()))
elif vocal == 'i' and 'I':
    print (frase.replace(vocal,vocal.upper()))
elif vocal == 'o' and 'O':
    print (frase.replace(vocal,vocal.upper()))
elif vocal == 'u' and 'U':
    print (frase.replace(vocal,vocal.upper()))
else: 
    print ("ERES SUBNORMAL")
