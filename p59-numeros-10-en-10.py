# Se desea imprimir los números de 1 a n de 10 en 10 mediante un ciclo for

n = int(input("Dame un número: "))
i = 1

for _ in range(n):
    if i > n:
        break
    print(i, end=" ")
    i += 10