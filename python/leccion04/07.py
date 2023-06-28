"""
Imprima los valores pares de una secuencia de numeros del 1 al 6
La secuencia continue
"""
for item in range(8):
    if item % 2 == 0:
        print(f'el {item} es par')
        continue
else:
    print("fin del ciclo ")