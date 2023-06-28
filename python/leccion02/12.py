# Se puede hacer la forma simplificada del and
# Esto es
"""
Ejercicio: Escribir un programa para definir si un usuario esta entre los 20 o entre 30's
Preguntar al usuario su edad

"""
edad = int(input("Escribe tu edad: "))
#veintes = edad >=20 and edad <30

# Se pone el operador en medio
var = 20 <= edad < 30
print(var)
#treintas = ed2ad >= 30 and edad <40
if (20 <= edad < 30) or (30 <= edad < 40):
    print("dentro de lo 20 o 30")
else:
    print("Fuera del rango")