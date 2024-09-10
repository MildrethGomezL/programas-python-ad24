import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear') 
    n = int(input('¿Hasta qué tabla quieres? '))
    m = int(input('¿Hasta dónde la quieres? '))

    t = 1
    while t <= n:
        print(f'\nTabla del {t}\n')  
        c = 1
        while c <= m:
            print(f'{t} x {c} = {t * c}') 
            c += 1
        t += 1

    res = input('\n¿Deseas continuar (S/N)? ')
    if res.upper() == 'N': 
        break

print("\nGracias por utilizar este programa...")