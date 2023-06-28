"""
La expresion continue es para saltarse el bloque de código
Imprimir todos aquellos números que son par
"""
for item in range(10):
    if item % 2 != 0:
        continue
    print(f'El número {item} es par')
