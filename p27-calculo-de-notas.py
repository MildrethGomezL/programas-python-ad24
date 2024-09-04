# Promedio de 5 calificaciones e imprimir un mensaje acorde al desempeño

print("Introduce tus 5 calificaciones para darte tu promedio ")

c1, c2, c3, c4, c5 = map(float, input().split())
promedio = (c1+c2+c3+c4+c5)/5
print(f'{promedio}')

if promedio <6:
    print(f'\nPromedio de {promedio} Quedas reprobado')
elif promedio <=7:
    print(f'\nPromedio de {promedio} Pasas de panzaso')
elif 7 < promedio < 8:
    print(f'\nPromedio de {promedio} Muy bien, Puedes mejorar')
elif 8< promedio < 9: 
    print(f'\nPromedio de {promedio} Excelente, sigue asi')
elif 9< promedio <=10: 
    print(f'\nPromedio de {promedio} Perfecto tu esfuerzo valió la pena')