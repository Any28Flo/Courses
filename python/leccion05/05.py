# Existe un nuevo tipo de dato llamado set
# Set es similar a una lista, pero tiene una peculiaridad
# No permite elementos duplicados
# Los elementos son desorganizados
# No puedes acceder a un elemento en específico, pero si al set
# Puedes agregar o eliminar elementos
frutas = {'Manzana', 'Pera', 'Mandarina'}
print(frutas)
# Para agregar elementos a el set
frutas.add('Manzana')
# Podemos saber la longitud
print(len(frutas))
# Podemos validar si un elemento existe dentro del set
# Podemos hacer lo mismo para las listas y las tuplas
print('Peras' in frutas)
# Podemos eliminar elementos
# Acá nos manda un error
# Por que no existe el elemento
#frutas.remove('Peraw')
#print(frutas)
# Sin embargo podemos utilizar el metodo discard
# discard no nos arrojara algun error
frutas.discard('Mandarinas')
print(frutas)
# Se puede limpiar el set
frutas.clear()
print(frutas)
# Se puede eliminar de la memoria
del frutas
print(frutas)