#  Resources S3 - version 1.0
#  Importer les variables 
import boto3
from flask import session
# Importer les variables définies dans config.py 
from config import S3_BUCKET, S3_KEY, S3_SECRET

# Fonction client S3 (définission de l'ID avec la clé Secret)
def _get_s3_resource():
    if S3_KEY and S3_SECRET:
        return boto3.resource(
            aws_access_key_id=S3_KEY, 
            aws_secret_access_key=S3_SECRET
                        )
        
    else:
        return boto3.resource('s3')

# Focntion mettre en place un variable resource s3
def get_bucket():
    s3_resource = _get_s3_resource()
    if 'bucket' in session:
        bucket = session['bucket']
    else:
        bucket = S3_BUCKET

    return s3_resource.Bucket(bucket)

# Fonction liste des buckets
def get_buckets_list():
    client = boto3.client('s3')
    return client.list_buckets().get('Buckets')
