

import random
import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  
    numero_secreto = random.randint(1, 100)  
    intentos = 0

    while True:
        numero_ingresado = int(input("Adivine el número secreto (1-100): "))
        intentos += 1

        if numero_ingresado == numero_secreto:
            print(f"\n¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        elif numero_ingresado < numero_secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")


    if not input("\n¿Deseas seguir jugando (S/N)? ").upper().startswith("S"):
        break

print("\nGracias por jugar.")