"""
Crear una función para multiplicar los valores recibidos de tipo númerico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la multiplicacion de todos los valores pasados como
argumento
"""


def multiplication(*args):
    total = 1
    for value in args:
        total *= value
    return total


response = multiplication(1, 2, 3, 4)
print(f"response : {response}")

response_2 = multiplication(3,5,15)
print(f"response : {response_2}")
