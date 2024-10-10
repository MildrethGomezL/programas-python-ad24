
# Creación del diccionario con las ventas
ventas = {
    "Juan": 1550,
    "Jose": 2600,
    "Maria": 2220
}

print("Diccionario inicial:", ventas)

#usando []
ventas["Rocio"] = 2500
ventas["Mateo"] = 1567

#usando update()
ventas.update({"Andrea": 9567})
ventas.update({"Miguel": 1234})


print("Diccionario modificado:", ventas)