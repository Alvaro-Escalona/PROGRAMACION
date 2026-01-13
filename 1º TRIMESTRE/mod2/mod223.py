# Diseña un algoritmo en el que, dadas tres personas, por ejemplo Pedro, Alicia y Carla,
# indique quiénes son de la misma quinta.

edad=int(input("Introduce la edad de la primera persona: "))
edad2=int(input("Introduce la edad de la segunda persona: "))
edad3=int(input("Introduce la edad de la tercera persona: "))

if edad == edad2 and edad == edad3:
    print("Las tres personas son de la misma quinta.")
elif edad == edad2:
    print("La primera y la segunda persona son de la misma quinta.")
elif edad == edad3:
    print("La primera y la tercera persona son de la misma quinta.")
elif edad2 == edad3:
    print("La segunda y la tercera persona son de la misma quinta.")
else:
    print("Ninguna de las personas es de la misma quinta.")