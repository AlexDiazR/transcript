import os
import whisper
from pytube import YouTube

model = whisper.load_model("base")
ytURL = "https://www.youtube.com/watch?v=sagpI6DSgeE"

def getTranscript(url):
  yt = YouTube(url)
  video = yt.streams.filter(only_audio=True).first()
  out_file=video.download(output_path=".")
  base, ext = os.path.splitext(out_file)
  new_file = base+'.mp3'
  os.rename(out_file, new_file)
  result = model.transcribe(new_file)
  output = result['text'].strip()
  os.remove(new_file)
  return output

transcript = getTranscript(ytURL)

print(transcript)

# Write into a text file
with open(f"download/videoTranscript.txt", "w", encoding="utf-8") as f:
 f.write(f"▼ Transcription of video\n")
 f.write(transcript)