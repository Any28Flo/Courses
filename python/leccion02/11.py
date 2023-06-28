"""
Ejercicio: Escribir un programa para definir si un usuario esta entre los 20 o entre 30's
Preguntar al usuario su edad

"""
edad = int(input("Escribe tu edad: "))
veintes = edad >=20 and edad <30
print(veintes)
treintas = edad >= 30 and edad <40
print(treintas)

if veintes or treintas:
    print(f"La edad {edad} esta dentro del rango")
    if(veintes):
        print("Esta dentro de los 20's")
    elif treintas:
        print("Esta dentro de los 30's")
else:
    print(f"La edad {edad} esta fuera del rango")
