"""
Las listas en python se definen dentro de corchetes []
y dentro pueden ir los datos que queramos
"""
# Definicion
nombre = ["Juan", "Pedro", "Armando", "Lupita", "Patricio", "Pedro", "Pedro"]

print(nombre)
# Podemos acceder a cualquiera de los elementos
# indicando el indice
print(nombre[2])

# Python tiene una peculiaridad y es que se puede acceder a los
# ultimos elementos de derecha a izquierda y para hacer eso el ultimo
# elemento será el -1 en orden ascendente
# Se accede al ultimo elemento del lado derecho

print(nombre[-1])

print(nombre[-2])

# Podemos imprimir rangos de valores
# Esto es excluyente , que no se tomara el ultimo elemento
# la condicion es < al elemento
# Imprime todos los elementos desde el 0 hasta <3
# Juan, pedro , armando
print(nombre[0:3])

# Esta la forma simplificada donde 0 se asume como el inicio
# Este recorrdo tambien es excluyente

print(nombre[:3])

# Podemos recorrer el array indicando el inicio y el fin
# Este recorriedo tambien es excluyente
print(nombre[2:4])

# El otro recorrido que podemos hacer es indicar el inico
# y si no le pasamos el parámetro estamos diciendo que recorre hasta
# el final
print(nombre[1:])

# Al igual que en js si queremos cambiar el valor de un elemento
# es necesario indicar la posición y el nuevo elemento
nombre[0] = "Arenita"
print(nombre)

# Una cosa es imprimir y otra es iterar para iterar podemos hacerlo con un loop
for item in nombre:
    print(f'{item}')

# Los arrays tienen tambien diferentes métodos que ya estan preechos
# Para poder acceder a estos elementos podemos acceder con .

# Para poder saber la longitud podemos hacer uso de la función len

print(len(nombre))

#  array.append -> Agrega un elemento al final
nombre.append("Don cangrego");
print(nombre)

# array.append -> Agrega un elemento before posicion i
# array.append[index, element]
nombre.insert(2, "Gary")
print(nombre)
# array.pop(index) -> Remueve elemento con el index
# remueve el primer elemento de la derecha
nombre.pop()
# remueve el elemento donde esta el index
nombre.pop(-2)
#Remueve patricio y don cangrejo
print(nombre)
# array.remove a diferencia de pop
# Remueve la primera ocurencua
nombre.remove("Pedro")
# Va a remover la de la posicion 1
print(nombre)
del nombre[-1]

print(nombre)
# Del se le puede pasar un rango
del nombre[0:2]
print(nombre)

# La funión clear limpia el arreglo de elementos
""
nombre.clear()
print(nombre)
# es limpiado el espacio de memoria asignado para la variable
del nombre
print(nombre)
