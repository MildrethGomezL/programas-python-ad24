
# Iterar sobre los elementos de la lista
import os
os.system('clear')


nums = [2, 4, 6, 8, 10, 12, 14, 16]
print(f'Todos los números: {nums}\n')

print('Iterar por elementos:')
for n in nums:
    print(n)

print('\nIterar por índice:')
for i in range(len(nums)):
    print(nums[i])

print('\nIterar por elementos sumando 2:')
for n in nums:
    print(n + 2)

print('\nIterar por índice sumando 10:')
for i in range(len(nums)):
    print(nums[i] + 10)