"""
La palabra reservada break sirve para "romper" la ejecución del programa

"""
cadena = "Holanda"

for item in cadena:
    if item == 'a':
        print(f'item: {item}')
        # Al momento que encuentra la condición se rompe y no se ejecuta más
        # el programa
        break
else:
    print("fin loop")