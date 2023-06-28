"""
Instrucciones de la tarea:
El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:

El usuario proporcionara un valor entre 0 y 10.
Si esta entre 9 y 10 imprimir una A
Si esta entre 7 y menor a 8 imprimir B
Si esta entre 6 y menor a 7 imprimir una D
Si esta entre 6 y menor a 7 imprimir una D
Si esta entre 0 y y menor a 6 imprimir una F
cualquier otro valor debe imprimar valor incorrecto

Por ejemplo proporciona un valor entre 0 y 10
A

"""
calificacion = int(input("Proporciona un valor entre 0 y 10: "))
calificacionLetra = ""

if (calificacion >= 0 ) and (calificacion < 6):
    calificacionLetra = "F"
elif (calificacion >= 6  ) and (calificacion <7):
    calificacionLetra = "D"
elif (calificacion >=7 ) and (calificacion <=8 ) :
    calificacion = "B"
elif (calificacion >=9 ) and (calificacion <= 10) :
    calificacion = "A"
else:
    calificacion = "Valor incorrecto"

print(f"Calificacion {calificacion}  - {calificacionLetra}")