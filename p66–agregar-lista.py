# Agregar elementos a la lista
import os
os.system('cls')

print('Agregar elementos a una lista existente \n')
num = [80.3, 12.5, 60.2, 30.4]


print(f'Todos los números: {num}\n')

num.append(90)
num.append(100)
print(f'Agregar al final: {num}\n')


num.insert(4, 80)
print(f'Insertar el número 80 en el índice 4: {num}\n')
o = [110, 120, 130]
num.extend(o)
print(f'Extender con {o}: {num}\n')