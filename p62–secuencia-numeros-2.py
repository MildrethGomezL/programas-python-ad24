# Se desea imprimir la secuencia de números según el número de renglones que el usuario desee

n = int(input("Dame un número: "))


for i in range(1, n + 1): 
    
    for j in range(1, i + 1):
        print(j, end=" ") 
    print()