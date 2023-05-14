import boto3

from constans import DATA_FILENAME

BUCKET = "pystravans"
KEY = "front/data.csv"
REGION = "us-east-2"

def upload_file_to_s3():
    S3 = boto3.client('s3', region_name=REGION)
    S3.upload_file(DATA_FILENAME, BUCKET, KEY)
