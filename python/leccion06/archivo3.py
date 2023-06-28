import boto3
ec2= boto3.client('ec2')
nombre_llave ='llave.pem'
ec2.delete_key_pair(KeyName = nombre_llave)
llaves = ec2.create_key_pair(KeyName=nombre_llave)
llave - llaves['KeyMAterial']
carga_llave= open(nombre_llave, 'w')
carga_llave.write(llaves)