
#Conjetura de collatz

import os

while True:
    os.system('cls') 
    print('Imprime la conjetura de Collatz')
    num = int(input('Dame un número: '))
    
    
    while num != 1:
        print(num, end=' ')
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    
    print(num)  
    
   
    res = input('\n¿Desea continuar (S/N)? ')
    if res.upper() == 'N': 
        break