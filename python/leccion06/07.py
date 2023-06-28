########## codigo clase 1
import boto3 as bt3
import os

#2 configurar credenciales
#ACCESS_KEY="AKIAQVR2O5GIITSZLP77"
#SECRET_KEY="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"
#region='us-east-1'
#bt3.Session(
#    aws_access_key_id=ACCESS_KEY,
#    aws_secret_access_key=SECRET_KEY,
# 	region_name=”us-east-1”)
print("La sesion ha sido configurada adecuadamente")
#2 crear  archivos y bucket
#creacion de archivos
region="us-east-1"
for i in range(0,10):
    nombre="texto"+str(i)+".txt"
    command="touch"+" "+nombre
    os.system(command)
print("archivos creados")
nombre_bucket="mi-primer-balde"
#creacion bucket
s3=bt3.client('s3',region_name=region)
s3.create_bucket(Bucket=nombre_bucket,
ACL="public-read")
#subir archivos
archivos=os.listdir()
for archivo in archivos:
    try:
        ruta="/home/ec2-user/environment/"+str(archivo)
        print(ruta)
        s3.upload_file(Filename=str(ruta),Bucket=nombre_bucket,Key=archivo)
    except:
        continue
print("creación exitosa")