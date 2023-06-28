archivos = os.listdir()
s3= boto3.client('s3')

for archivo in archivos:
    try:
        s3.put_boject_acl(Bucket='mi-primer-balde', Key = archivo, ACL='public-read')
        print(archivo)
    except:
        continue
    print('Archivos actualizados')