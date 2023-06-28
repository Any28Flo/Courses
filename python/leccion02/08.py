# Los operadores logicos de python son
# and -> Devuelve true si ambos operandos son True
a = True
b = True
resultado = a and b
print(f'operando and {a} and {b} : {resultado}')

# or -> Devuelve True si alguno de los operadores es True
b = False
resultado = a or b
print(f'operando or {a} or {b} : {resultado}')

# not -> Devuelve True si alguno de los operandos es False
# Hace la negacion del valor
resultado = not a
# a -> True
print(f'operando not {a}: {resultado}')
resultado = not b
# b -> False
print(f'operando not {b}: {resultado}')
