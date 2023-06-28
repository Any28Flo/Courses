"""
Instrucciones:
Solicitar al usuario dos valores y determinar cual es mayor
Se debe imprimir el mayor de los dos numeros

"""
num1 = int(input("Proporciona el numero 1 : "))
num2 = int(input("Proporciona el numero 2: "))

if num1 > num2:
    print(f"El {num1} es mayor")
elif num2 > num1:
    print(f"El numero {num2} es mayor")
else:
    print("son iguales")