# Realizar las operaciones

import os; os.system('clear')

muns = {'Zacatecas','Guadalupe', 'Jerez','Fresnillo'}

print ('El conjunt: ',muns, len(muns))

print('Lista de municipios')
for mun in muns:
    print(mun, end=' ')

print('\Esta Zacatecas en los municipios  - ','Zacatecas'in muns)

muns.add('teul')
print('El conjunt : ', muns, len(muns))

mas ={'luis moya','ojocaliente','tepetongo','rio grande'}

muns.update(mas)
print('El conjunto : ', muns, len(muns))

muns.remove('luis moya')
print('El conjunto : ', muns, len(muns))

muns.discard('luis moya')
print('El conjunto : ', muns, len(muns))

mun = muns.pop()
print(mun)
print('El conjunto : ', muns, len(muns))

muns.clear()
print('El conjunto : ', muns, len(muns))