from elevenlabs import ElevenLabs
client = ElevenLabs(api_key="sk_870a148cf2f8994b6603bf58466da95608d861e80636b31c")
x = client.speech_to_text.convert(model_id="scribe_v1", file=open("a2.mp3","rb"), num_speakers=2, diarize=True)

print(x)
exit(0)
for i in x.words:
	print(i.text, i.speaker_id)
