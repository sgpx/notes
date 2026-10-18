from pathlib import Path
from openai import OpenAI
client = OpenAI("YOUR API KEY HERE!")

txt = "Pizza Time!"


speech_file_path="speech.mp3"

response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=txt
)

response.stream_to_file(speech_file_path)
