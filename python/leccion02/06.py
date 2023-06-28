"""
Verifica si un numero es par o impar
Pida al usuario un numero
Verifique que el numero sea par o impar
    Si es par imprimir : es PAR
    de lo comtrario : es IMPAR

"""

num = int(input('Ingresa un numero: '))
if num % 2 == 0:
    print(f'El numero {num} es PAR ')
else:
    print(f'El numero {num} es IMPAR')
