# Se desea imprimir los pares de 2 a n y su suma

n = int(input("Dame un número: "))
suma = 0
i = 2

while i <= n:
    print(i, end=" ")
    suma += i
    i += 2

print(f", La suma es = {suma}")