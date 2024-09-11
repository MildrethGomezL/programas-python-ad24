# Imprimir los numeros impares hasta N numero

while True:
    n = int(input("Introduce un número positivo para imprimir los números impares hasta ese número: "))

    suma_impares = 0
    i = 1

    print("Números impares:")
 
    while i <= n:
        if i % 2 != 0:  
            print(i, end=" ")
            suma_impares += i
        i = i +1 

    print("\nSuma de los números impares:", suma_impares)

    repetir = input("¿Quieres repetir el proceso? (s/n): ")
    if repetir.lower() != 's':
        break

print("Programa finalizado.")