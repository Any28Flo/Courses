"""
Instrucciones
- En el siguiente ejercicio se solicita calcular el area y el perimetro de un rectangulo,
alto (int)
ancho (int)
- El usuario debe proporcionar los valores de largo y ancho, y despues debe imprimir el resultado
en el siguiente formato ( no usar acentos y respetar los espacios , mayusculas, minusculas y saltos de
linea)
Proporciona el alto:
Proporciona el ancho:
Area : <area>
Perimetro: <perimetro>

Las formulas para calcular el area y el perimetro de un rectangulo son:
area: alto * ancho
perimetro: (alto + ancho ) * 2

 """
alto = int(input("Proporciona el alto: "))
ancho = int(input("Proporciona el ancho: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f'Area: {str(area)}')
print(f'Perimetro: {str(perimetro)}')

