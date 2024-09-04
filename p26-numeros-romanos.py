# Numero romano del 1 al 10 

numero = int(input("Ingresa un número entre 1 y 10: "))

def num(numero):
    dias = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
    }
    
    if numero in dias:
        return dias[numero]
    else:
        return "Numero inválido"




print(num(numero))