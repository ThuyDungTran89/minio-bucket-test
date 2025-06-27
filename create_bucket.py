import boto3
from botocore.exceptions import ClientError

# Cau hinh MinIO
MINIO_ENDPOINT = "http://localhost:9000"
ACCESS_KEY = "minioadmin"
SECRET_KEY = "minioadmin"
BUCKET_NAME = "voice-call"

# Tao client
s3 = boto3.client(
    's3',
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)

# Tao bucket
try:
    s3.head_bucket(Bucket=BUCKET_NAME)
    print(f"Bucket '{BUCKET_NAME}' da ton tai roi")
except ClientError:
    s3.create_bucket(Bucket=BUCKET_NAME)
    print(f"Da tao bucket: '{BUCKET_NAME}'")

