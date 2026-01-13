# Multiplicar sin usar el símbolo * (dos números)

def multiplicar (n1, n2):
    resultado = 0
    for i in range (n2):
        resultado = resultado + n1
    return resultado
# Programa principal

n1 = int(input("Introduce un numero: "))
n2 = int(input("Introduce un numero: "))

print ("La multimplicacion es ", multiplicar(n1,n2))