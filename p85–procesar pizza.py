# Procesar pizza
import os
os.system('cls')

# Diccionario de ingredientes y sus precios
ingr = {'T': 1.50, 'P': 3.50, 'C': 3.74, 'A': 0.40}
base = 15  
st = 0 
tot = 0  


pedido = input('Ingredientes de tu pizza? ').upper()

for i in pedido:
    if i in 'TPCA':
        st += ingr[i]

st += base

if st >= 20:
    tot = st - (st * 0.05)  
else:
    tot = st  

# Mostrar el subtotal y el total
print(f'El subtotal es: {st}')
print(f'El total es: {tot}')