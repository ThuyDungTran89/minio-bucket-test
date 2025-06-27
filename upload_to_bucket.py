import boto3
from botocore.exceptions import NoCredentialsError

# Thông tin cấu hình MinIO
MINIO_ENDPOINT = "http://localhost:9000"
ACCESS_KEY = "minioadmin"
SECRET_KEY = "minioadmin"
BUCKET_NAME = "voice-call"

FILE_PATH = "D:\\MinIO-Project\\Test TD.mp3"
OBJECT_NAME = "D:\\Test TD.mp3"

# Tạo client
s3 = boto3.client(
    "s3",
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)

# Upload
try:
    s3.upload_file(FILE_PATH, BUCKET_NAME, OBJECT_NAME)
    print(f"Đã upload '{FILE_PATH}' vào bucket '{BUCKET_NAME}'")
except FileNotFoundError:
    print("Không tìm thấy file.")
except NoCredentialsError:
    print("Lỗi xác thực.")
except Exception as e:
    print(f"Lỗi khác: {e}")
