# Otro tipo de dato son los diccionarios
# Los diccionarios se caracterizan por tener llave-valor
diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'

}
valores ={
    1: 'valor 1',
    2: 12,
    3: True

}
# Para poder ver la longitud de un diccionario
longitud = len(diccionario)
print(longitud)

# Para poder acceder a un elemento del diccionario
valor = diccionario['IDE']
print(valor)

for item in valores:
    print(valores[item])

# es necesario conocer el valor de la llave para poder acceder al elemento
# a diferencia de las listas, tuplas, los diccionarios inician desde el índice 1
print(valores[3])
# El key es keysensitive
print(diccionario['OOP'])
# Otro método por el cuál podemos acceder a los elementos es con el método get
print(diccionario.get('DBMS'))

# Para poder iterar sobre los elementos de un diccionario podemos:
# Recorrer con llave-valor
# Ya hay built-in functions asociadas a los elementos como:

# .items() -> nos permite recorrer los elementos de un diccionario

for (item, value) in diccionario.items():
    print(f'{item}:{value}')

# .keys ->Para obtener las llaves

for item in diccionario.keys():
    print(item)

# .values() ->Para obtener los valores

for item in diccionario.values():
    print(item)

# Podemos definir un diccionario con las {}
gamesThrones={}
# Para agregar un elemento definimos la llave y el valor
gamesThrones['character'] = 'Sansa Stark'
gamesThrones['evilness'] = 0
print(gamesThrones)
# Podemos cambiar los valores de los diccionarios ya que son mutables
# Insertamos el key y el nuevo valor, esto sobreescribe los valores anteriores

gamesThrones['evilness'] = 5
print(gamesThrones)

# Podemos remover un elemento con el método
# pop
gamesThrones.pop('evilness')

print(gamesThrones)

# Podemos limpiar los valores que tiene asignados

# gamesThrones.clear()
# Si ya no necesitamos un campo podemos borrar el key
# Esto borrara el valor
del gamesThrones['evilness']
# Podemos limpiar el espacio de memoria asignado a ese elemento
# del gamesThrones
print(gamesThrones)