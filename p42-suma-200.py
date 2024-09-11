# suma cantidades x siempre y cuando no pase de 200
while True:
   
    suma = 0
    contador = 0

    print("Introduce números enteros para sumarlos hasta que sea >= 200.")

    while suma < 200:
        numero = int(input("Introduce un número entero: "))

        suma += numero
        contador += 1

    print(f"Suma total de los números: {suma}")
    print(f"Números introducidos: {contador}")

    repetir = input("¿Quieres repetir el proceso? (s/n): ")
    if repetir.lower() != 's':
        break

print("Programa finalizado.")