
# Creación del diccionario con llaves con los países y sus valores

paises = {
    "Argentina": 100,
    "Brasil": 200,
    "Colombia": 300,
    "Chile": 400,
    "Ecuador": 500,
    "Bolivia": 600,
    "Jamaica": 700
}

# Mostrar el diccionario inicial
print("Diccionario inicial:", paises)

#usando []
paises["Brasil"] = 250
paises["Chile"] = 450

#usando update
paises.update({"Bolivia": 650})
paises.update({"Jamaica": 750})

print("Diccionario modificado:", paises)