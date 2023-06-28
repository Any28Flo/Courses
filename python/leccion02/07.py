"""
    Determine si es mayor de edad

    Pida al usuario una edad
    "Escribe tu edad"
    Verifique si es mayor de edad
    Si es correcto "Eres mayor de edad"
    de lo contrario "Eres menor de edad"

"""
edadAdulto = 18
age = int(input("Escribe tu edad: "))
if age >= edadAdulto:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
