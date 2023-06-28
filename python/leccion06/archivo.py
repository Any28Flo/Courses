import os
import boto3
ec2_client=boto3.client('ec2')
llave=ec2_client.create_key_pair(KeyName="llave")
llave_f=str(llave)
orden="echo" +" "+str(llave_f)+" "+">"+"llave.pem"
os.system(orden)

import os
import boto3
ec2_client=boto3.client('ec2')
llave=ec2_client.create_key_pair(KeyName="llave")
llave_f=str(llave)
orden="echo" +" "+str(llave_f)+" "+">"+"llave.pem"
os.system(orden)