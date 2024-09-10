#Convertir en pesos a dolar

import os

while True:
    os.system('clear')  
    tc = 20.71 
    pi = float(input("Valor inicial en pesos: "))
    pf = float(input("Valor final en pesos: "))
    
    c = pi
    print("\nPesos\tDollar")
    print("-" * 15)
    
    while c <= pf:
        print(f'{c:.2f}\t{c/tc:.2f}')  
        c += 1  
    
    print("-" * 15)
    
  
    res = input('Deseas continuar (S/N)? ')
    if res.upper() == 'N':  
        break