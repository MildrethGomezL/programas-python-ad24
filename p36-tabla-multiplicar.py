#Tablas de multiplicar hasta donde se requiera

import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  
    t = int(input('¿Qué tabla quieres? '))
    n = int(input('¿Hasta dónde la quieres? '))
    
    c = 1
    while c <= n:
        print(f'{t} x {c} = {t * c}')
        c += 1  

    res = input('¿Desea continuar (S/N)? ')
    if res.upper() == 'N':
        break

print("Gracias por utilizar este programa...")