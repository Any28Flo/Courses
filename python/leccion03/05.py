"""
Ejercicio determine la estacion del año de acuerdo al mes ingresado
Los numeros del año seran en número del 1-12
Las estaciones del año son Primaver, Verano, Otoño e Invierno

"""
mes = int(input("Ingrese el mes: "))
estacion = ""
if (mes >= 3) & (mes <= 6):
    # Primavera
    estacion = "Primavera"
elif (mes >= 7) & (mes <= 9):
    estacion = "Verano"
elif (mes >= 10) & (mes <= 12):
    estacion = "Otoño"
elif (mes >= 1) & (mes <= 2):
    estacion = "Invierno"
else:
    estacion = "Valor no valido "

print(f"Estacion {estacion}")