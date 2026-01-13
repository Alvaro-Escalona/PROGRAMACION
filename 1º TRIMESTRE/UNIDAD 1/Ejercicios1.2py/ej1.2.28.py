#Calcular el área de un triángulo a partir de tres lados 



a = float(input("Introduce el largo del lado a: "))
b = float(input("Introduce el largo del lado b: "))
c = float(input("Introduce el largo del lado c: "))


suma = (a + b + c) / 2

area = (suma * (suma - a) * (suma - b) * (suma - c)) ** 0.5
if area==0:
    print("No se puede calcular el area con un lado igual a 0")
else:
    print(f"El área del triángulo es: {area:.2f}")