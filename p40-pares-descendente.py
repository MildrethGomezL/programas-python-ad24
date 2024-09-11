while True:
    n = int(input("Introduce un número menor que 100 para imprimir los números pares desde 100 hasta ese número: "))

    if n >= 100:
        print("Por favor, introduce un número menor que 100.")
        continue

    suma_pares = 0
    i = 100

    print("Números pares:")
    
    while i >= n:
        if i % 2 == 0:  
            print(i, end=" ")
            suma_pares = suma_pares + i
        i =  i - 1

    print(f"\nSuma de los números pares: {suma_pares}")

    repetir = input("¿Quieres repetir el proceso? (s/n): ")
    if repetir.lower() != 's':
        break

print("Programa finalizado.")