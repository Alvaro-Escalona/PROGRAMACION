#En una determinada empresa, sus empleados son evaluados al final de cada año. Los 
# puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
# traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados 
# pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
# A continuación, se muestra una tabla con los niveles correspondientes a cada 
# puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada 
# por la puntuación del nivel. 

import os

def beneficio(puntos):
    sueldo= 2400
    if puntos==0.0:
        return sueldo+(sueldo*0.0)
    elif puntos==0.4:
        return sueldo+(sueldo*0.4)
    else:
        puntos==0.6
        return sueldo+(sueldo*0.6)
    
# Programa principal

if __name__=="__main__":

    os.system("cls")

    try:
        puntos = float(input("Introduce los puntos obtenidos en la evaluación: "))
        sueldo = beneficio(puntos)
        print(f"Tu beneficio es de {sueldo}€")
    except ValueError:
        print("Por favor, introduce un número.")    
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
    