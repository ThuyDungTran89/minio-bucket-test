import whisper

# Path file audio
AUDIO_PATH = "D:/MinIO-Project/Test TD.mp3"

# Load model
model = whisper.load_model("medium")

# Tieng Viet ghi VI
result = model.transcribe(AUDIO_PATH, language="vi")

# In
print("\n=== Van ban tu giong noi ===")
print(result["text"])
