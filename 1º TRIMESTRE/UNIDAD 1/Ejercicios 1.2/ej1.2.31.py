from sympy import isprime

n=int(input("Introduce un número: "))

if isprime(n):
    print(f"Es primo y no tiene divisor, el unico es él mismo: {n}")
else:
    if (n<4):
        print("Demasiado pequeño, introduce otro número")
    else:
        i=2
        while (i<=n):
            if (n%i==0):
                print("{:3d} es un divisor".format(i))
                n=n//i
            else:    
                i=i+1