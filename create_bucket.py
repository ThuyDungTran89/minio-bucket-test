import boto3
from botocore.exceptions import ClientError

# Cấu hình MinIO
MINIO_ENDPOINT = "http://localhost:9000"
ACCESS_KEY = "minioadmin"
SECRET_KEY = "minioadmin"
BUCKET_NAME = "voice-call"

# Tạo client
s3 = boto3.client(
    's3',
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)

# Tạo bucket nếu chưa có
try:
    s3.head_bucket(Bucket=BUCKET_NAME)
    print(f"Bucket '{BUCKET_NAME}' đã tồn tại.")
except ClientError:
    s3.create_bucket(Bucket=BUCKET_NAME)
    print(f"Đã tạo bucket: '{BUCKET_NAME}'")

