"""
Escriba un programa en python que imprima la etapa de la vida correspondiente
0-10 : La infancia es increible
10-20 : Muchos cambios y mucho estudio...
20-30 : Amor y comienza el trabajo
Cualquier otro valor: Etapa de la vida no reconocida
"""
edad = int(input("Proporciona tu edad: "))
etapa = ""

if (edad >= 0) & (edad <= 10):
    etapa = "La infacia es increible"
elif (edad >= 11) & (edad <= 20):
    etapa = "Muchos cambios y mucho estudio"
elif (edad >= 21) & (edad <= 30):
    etapa = "Amor y comienza el trabajo"
else:
    etapa = "Etapa de la vida no reconocida"

print(f"Etapa de la vida de la edad: {edad} : {etapa}")
