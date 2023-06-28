"""
Escriba un programa que de la salida sea:
Proporcione los siguientes datos del libro:
Proporiona el nombre
Proporciona el ID
Proporcione el precio
Indica si el envio es gratuito (True / False)

"""
print("Proporcione los siguientes datos del libro")
nombre = input("Proporciona el nombre: ")
id = int(input("Proporciona el ID: "))
precio = float(input("Proporciona el precio:"))
envioGratuito = input("Indica si el envio es gratuito (True/False): ")
# No se puede hacer una conversion inline porque si no se ingresa un valor lo marcara como falso
# no -> bool(input("envio gratuito))
# se tiene que hacer una validacion externa

if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'Valor no valido, debe escribir True/False'
# Se puede escribir los valores de la siguiente forma

# print(nombre)
# print(id)
# print(precio)
# print(envioGratuito)
# Pero si se quiere que sea un comentario multilinea se hara
print(f"""
nombre : {nombre}
id: {id}
precio : {precio}
envio gratuito : {envioGratuito}
""")
