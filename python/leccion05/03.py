# Las tuplas son similares a las listas en python con la peculiaridad
# De que las tuplas son inmutables
# Para definir una tupla se define con ()
tupla = ('Mesi', 'Ronaldo', 'Di Maria', 'Pele')
print(type(tupla))
for item in tupla:
    print(item)

# Se pueden acceder a los elementos por medio del índice
# Di Maria
print(tupla[2])
# Al momento de imprimir por los números negativos
# Se recorre de lado inverso
# Ronaldo

print(tupla[-2])

# Se puede ocupar los rangos para imprimir valores de la tupla
print(tupla[1:3])

# Se pueden recorrer todos los elementos de la tupla con los loop
for item in tupla:
    # Print acepta otro parámetro (end) que es el caracter de espacio
    print(item, end=' ')

# Recordemos que las tuplas no se pueden modificar
# Insertar un núevo elemento
# tupla[0] = 'Licha Cervantes'
# Nos dara un error
# print(tupla)

# Si queremos agregar o editar una tupla lo que se tiene que hacer es un parse
# Convertir la tupla a lista y vise berza
tuplaLista = list(tupla)

# Cambiamos el elemento
tuplaLista[0] = 'Licha Cervantes'

# Viceverza
tupla = tuple(tuplaLista)
print('\n')
print(f'tipo : { type (tupla)} , valor {tupla}')

# La función que si sirve para las tuplas es del
# del-para borrar un elemeto
del tupla
print(tupla)
