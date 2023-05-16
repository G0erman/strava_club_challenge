import boto3

from constans import DATA_FILENAME

BUCKET = "pystravan-silver"
KEY = "data.csv"
REGION = "us-east-2"
ARGUMENTS = {'ACL': 'public-read'}

def upload_file_to_s3(is_public=False):
    S3 = boto3.client('s3', region_name=REGION)
    try:
        if is_public:
            S3.upload_file(DATA_FILENAME, BUCKET, KEY, ExtraArgs=ARGUMENTS)
        else:
            S3.upload_file(DATA_FILENAME, BUCKET, KEY)
    except Exception as e:
        print("Something unexpected happened!", e)
