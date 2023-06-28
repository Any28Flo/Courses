
##Creacion de bucket
import boto3
s3= boto3.client('s3')
s3.create_bucket(Bucket='mi-primer-balde', ACL ="public-read")
s3.upload_file(Filenamee='/home/ec2-user/enviroment', Bucket="mi-primerbalde", Key="mipagina.html")
s3.put_objetct_acl(Bucket="mi-primer-balde", Key="mipagina.html", ACL="public-read")


