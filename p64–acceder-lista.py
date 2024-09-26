
import os
os.system('clear')
nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]

print('Acceder a los elementos de una lista\n')
print(f'Cantidad de números: {len(nums)} \n')
print(f'Todos los números: {nums} \n')
print(f'Primero y último número: {nums[0]}, {nums[-1]} \n')
print(f'Del índice 2 al 5: {nums[2:6]} \n')
print(f'Los primeros 3 números: {nums[:3]} \n')
print(f'Los últimos 3 números: {nums[-3:]} \n')