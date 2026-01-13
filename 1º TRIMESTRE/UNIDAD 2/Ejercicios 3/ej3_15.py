#  Crea un subprograma que reciba una nota decimal y devuelva si está suspenso, 
# aprobado, notable o sobresaliente. 

import os

def nota(a):
    if a < 5:
        return "suspenso"
    elif 5 <= a < 7:
        return "aprobado"
    elif 7 <= a < 9:
        return "notable"
    elif 9 <= a <= 10:
        return "sobresaliente"
    else:
        return "Nota inválida"
    
#  Programa principal

if __name__=="__main__":
    os.system("cls")

    n = float(input("Introduce una nota decimal (0-10): "))
    resultado = nota(n)
    print("La calificación es:", resultado)