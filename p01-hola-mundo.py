# p01-Hola-mundo - Recibe datos del usuario y los imprime en pantalla 

nombre = input("Dame tu nombre ")
edad = int( input("¿cual es tu edad? "))
peso = float( input("¿cual es tu peso? "))

print (nombre)
print(edad)
print(peso)
      
print(f"{nombre } bienvenido a python, tu edad es { edad} tu peso es we{ peso}")   

print(type(nombre))
print(type(edad))
print(type(peso))
