# Utilizando la funcion de range realice los siguientes ejercicios
# range(inicio<opcional> , fin <requerido>, incremento <opcinal>)

# Ejercico 1: Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
print('Rango de 0 a 10 con números divisibles entre 3')
for element in range(10):
    if element % 3 == 0:
        print(f'El {element} es multiplo de 3')

for element in range(10):
    if element % 3 != 0:
        continue
    print(f'El {element} es multiplo de 3')

print('Rango de números de 2 a 6 e imprimirlos')
# Ejercicio 2 : Crear un rango de números de 2 a 6 e imprimirlos
for element in range(2, 7):
    print(f'{element}')
print('Rango de 3 a 10 con incremento de 2 en 2 ')
# Ejercicio 3: Crear un rango de 3 a 10, pero con incremento de 2 en 2
for element in range(3, 10, 2):
    print(f'item {element}')