# Programa que calcula la suma y el promedio de una serie de numeros ingresados
while True:
    suma = 0
    contador = 0

    print("Introduce números enteros para calcular la suma y el promedio, para finalizar ingresa 0 ")

    while True:
        
        numero = int(input("Introduce un número entero: "))

        
        if numero == 0:
            break


        suma += numero
        contador += 1

    if contador > 0:
        promedio = suma / contador
        print(f"Suma de los números: {suma}")
        print(f"Promedio de los números: {promedio}")
        print(f"Números introducidos: {contador}")
    else:
        print("No se introdujeron números.")
    repetir = input("¿Quieres repetir el proceso? (s/n): ")
    if repetir.lower() != 's':
        break

print("Programa finalizado.")