import whisper

fileName = "sample4.mp3"#@param {type:"string"}
lang = "en"#@param ["en", "ja","es"]
model = whisper.load_model("base")

# Load audio
audio = whisper.load_audio(f"content/sample/{fileName}")
audio = whisper.pad_or_trim(audio)

mel = whisper.log_mel_spectrogram(audio).to(model.device)

# Output the recognized text
options = whisper.DecodingOptions(without_timestamps=True, fp16=False)
result = whisper.decode(model, mel, options)
print(result.text)

# Write into a text file
with open(f"download/{fileName}.txt", "w", encoding="utf-8") as f:
  f.write(f"▼ Transcription of {fileName}\n")
  f.write(result.text)