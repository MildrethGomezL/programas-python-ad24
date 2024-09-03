# Aceptar estudiante base a su edad y calificaciones
#>=18  c1>=8 y c2 >=8

import os; os.system("clear")

print("Universidad patito SA de CV")
print("Aceptar un estudiante base a su edad y dos calificaciones:\n")

nombre = input("Dame el nombre: ")
edad = int(input ("Dame la edad: "))

if edad >= 18 :
    print("Dame 2 calificaciones separadas por un enter ")
    c1, c2 = int(input()), int(input())
    if c1>=8 and c2>=8:
        print(f"{nombre} bienvenido a la universidad, tu edad {edad} y tus calificaciones {c1},{c2} lo permiten")
    else:
         print("\nSolo aceptamos con calificaciones mayores o iguales a 8")
else:
    print("\nSolo aceptamos mayores de edad  ")
              
print("\nGracias por utilizar este programa... ")

