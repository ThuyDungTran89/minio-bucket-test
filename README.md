"# MinIO Bucket Creator" 
# Voice Call Summarizer (MinIO + Whisper)

DSu dung MinIO de luu file ghi am cuoc hop va dung Whisper de chuyen thanh van ban (ASR).

# Cau truc
- 'create_bucket.py': Tao bucket tren MinIO
- 'upload_to_bucket.py': Upload file vao bucket
- 'transcribe_audio.py': Dung Whisper de chuyen giong noi thanh text
- 'requirements.txt': Cac thu vien can cai dat

#Cach thuc thi

# 1. Cai thu vien
'''bash
pip install -r requirements.txt
# 2. Tao bucket MinIO
python create_bucket.py
# 3. Upload file audio len bucket
python upload_to_bucket.py
# 4. Chuyen giong noi thanh van ban
python transcribe_audio.py

