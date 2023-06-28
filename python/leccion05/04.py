# Dada la siguiente tupla,
# Crear una lista que sólo incluya los números menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)
# 1,3,2,5,
menoresCinco = []
limit = 5
tuplaLista = list(tupla)
for element in tuplaLista:
    if element <= 5:
        menoresCinco.append(element)


print(menoresCinco)

tupla = tuple(menoresCinco)

print(tupla)
print(type (tupla))