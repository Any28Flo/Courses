"""
La sentencia de control if evalua si una condicon es verdadera o falsa
No necesariamente un valor booleano
si hay un valor, que sea de cualquier tipo el valor sera verdadero
Si no existe valor ( False, '') el valor sera falso
"""
valor = True
if valor:
    print("El valor es verdadero")
else:
    print("El valor es falso")

valorNulo = ''

if valorNulo:
    print("El valor es verdadero")
else:
    print("El valor es falso")

# Se pueden hacer bloques anidades o que evaluen varias condiciones
# Con el else if

