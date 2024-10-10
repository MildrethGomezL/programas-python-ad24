# Creación del diccionario con llaves nuemericas con los días de la semana

dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}


print("Diccionario completo:", dias)

print("Primer elemento usando []:", dias[1])
print("Último elemento usando []:", dias[7])

print("Quinto elemento usando get():", dias.get(5))
print("Séptimo elemento usando get():", dias.get(7))

print("Diccionario completo:", dias)