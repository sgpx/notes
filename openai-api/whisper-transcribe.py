from openai import OpenAI
from os import environ

oaikey = open("/tmp/mycompany_openai.txt", "r").read().strip()
environ["OPENAI_API_KEY"] = oaikey

client = OpenAI()

audio_file = open("a.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)

print(transcript)
