#calcular las funciones trigonometricas sobre un angulo
import math as mt

print("calcular las funciones trigonometricas sobre un angulo")

angulod = float(input("Dame un angulo "))
angulor = mt.radians(angulod)

print(f"Angulo original : {angulod}, angulo en radianes : {angulor}")

salida = ("Resumen de funciones trigonometricas \n"
          f"seno : {mt.sin(angulor):.3f} \n"
          f"coseno : {mt.cos(angulor):.3f} \n"
          f"tangente : {mt.tan(angulor):.3f} \n"
         )

print(salida)
                    