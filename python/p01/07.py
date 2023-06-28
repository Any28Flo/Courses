# Funcion input para procesar la entrada del usuario
valor = input()
print(valor)
# El valor tipo de valor que ingresa es de tipo str
age = input()
print(type(age))
# Puede ser confuso para el usuario que solamente esperemos un dato
# Por lo cual se le puede pasar un str a la funcion input
pet = input("Inserta el nombre de tu mascota: ")
print('El nombre de tu mascota es:' +pet)