"""
Crear una función para sumar los valores recibidos de tipo númerico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la suma de todos los valores pasados como
argumento
"""


def suma(*args):
    total = 0
    for arg in args:
        total += arg

    return total


sumaTotal = suma(2, 5, -1)
print(sumaTotal)

sumaTotal = suma(3, 5, 9, 4, 6)
print(sumaTotal)