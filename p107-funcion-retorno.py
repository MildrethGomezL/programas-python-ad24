# Funcion con parametros que regresa un valor 
import os

def suma(n1, n2):
    s = n1 + n2
    return s

os.system("cls")

#Resultado se guarda en una variable
r = suma(100,200)
print("El resultado es ", r)

#Resultado se calculo y se imprime
print("\nOtra suma ", suma(500,200))

#valor de los parametros
print("\nDame dos numeros a sumar separados por <enter> ")
a , b = int(input()), int(input())
print("\nLa suma del usuario es ", suma(a, b))

