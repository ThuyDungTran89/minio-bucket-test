import whisper

# Đường dẫn đến file audio
AUDIO_PATH = "D:/MinIO-Project/Test TD.mp3"

# Load model (có thể dùng: tiny, base, small, medium, large)
model = whisper.load_model("medium")

# Nếu là tiếng Việt hoặc tiếng Anh thì chỉ rõ
result = model.transcribe(AUDIO_PATH, language="vi")

# In kết quả
print("\n=== Văn bản từ giọng nói ===")
print(result["text"])