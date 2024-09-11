# Programa que dice cual numero es mayor de una serie de numeros introducidos 
repetir = 's'

while repetir.lower() == 's':
    
    mayor = None

    print("Introduce una serie de números enteros e introduce 0 para terminar")

    while True:
        numero = int(input("Introduce un número: "))

        if numero == 0:
            break
        if mayor is None or numero > mayor:
            mayor = numero

    if mayor is not None:
        print(f"El número mayor introducido fue: {mayor}")
    else:
        print("No se introdujeron números.")
    repetir = input("¿Quieres repetir el proceso? (s/n): ")

print("Programa finalizado.")