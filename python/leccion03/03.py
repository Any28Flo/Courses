"""
Ejercicio : Pida al usuario un número entre 1 y 3
Convierta el número a texto
1 = "Inserto el numero uno"
...
"""
numero = int(input("Ingrese un número entre 1 y 3: "))

numeroTexto = ''

if numero == 1:
    numeroTexto = "uno"
elif numero == 2:
    numeroTexto = "dos"
elif numero == 3 :
    numeroTexto = "tres"
else:
    numeroTexto = "Valor no valido"

print(f"Inserto el número  {numero}:{numeroTexto}")