"""
Ejercicio : Calculadora de impuestos
Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado
Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto /100)
"""

continuar = "T"


def calcular_impuesto(pago_sin_impuesto, impuesto):
    return pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)


def input_text(texto_imprimir):
    return float(input(texto_imprimir))


while continuar == 'T':
    pago_sin_impuesto = input_text("Ingrese pago sin impuesto: ")
    impuesto = input_text("Ingrese impuesto: ")
    pago_total = calcular_impuesto(pago_sin_impuesto, impuesto)
    print(f"El pago total es: {pago_total}")
    continuar = input("Continuar (False, True)")
