 # Imprimir la secuencia de términos armónicos 
import math
n = int(input("¿Cuántos términos? "))

#suma = 0

terminos = [4]

for i in range(1, n + 1):
    
    termino = 1 / math.factorial(i)
    
    terminos.append(f"1/{i}!")
    
    suma += termino
print(" + ".join(terminos), f", suma: {suma}")