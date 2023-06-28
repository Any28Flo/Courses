"""
Ejercicio: Convertidor de temperatura
Realizar dos funciones para convertir de grados celsius a farenheit y viceversa

"""


def fahrenheit_to_celcius(farenheit):
    return (farenheit - 32) / 1.800


def celcius_to_fahrenheit(celcius):
    return (celcius * 1.800) + 32.00


continuar = 'F'
grados = ""
opcion = ""
resultado = ""
opcion = input("Qué opcion quieres? : \n "
               "1. Fahrenheit a celcius\n"
               "2. Celcius a farenceit \n")
if opcion == '1':
    grados = "farenheit"
elif opcion == '2':
    grados = 'celcius'

valor = float(input(f"ingresa los grados {grados}"))
if opcion == '1':
    resultado = fahrenheit_to_celcius(valor)
    print(f"El resultado de °F a °C es :{resultado}")
elif opcion == '2':
    resultado = celcius_to_fahrenheit(valor)
    print(f"El resultado de °C a °F es :{resultado}")


