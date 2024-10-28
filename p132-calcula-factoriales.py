
def leer_lista():
   
    numeros = input("Dame los números: ")
    lista_numeros = list(map(int, numeros.split()))
    return lista_numeros

def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n+1):
            factorial *= i
        return factorial
    
def calcular_factoriales(lista_numeros):
    lista_factoriales = []
    for numero in lista_numeros:
        lista_factoriales.append(calcular_factorial(numero))
    return lista_factoriales

def main():
    
    lista_numeros = leer_lista()
   
    lista_factoriales = calcular_factoriales(lista_numeros)
    print("La lista de números originales:", lista_numeros)
    print("La lista con los factoriales:", lista_factoriales)

main()