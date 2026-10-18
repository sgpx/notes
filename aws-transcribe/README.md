# transcribe

`aws transcribe start-transcription-job --region ap-south-1 --transcription-job-name tju-1 --media '{"MediaFileUri":"s3://mybucket/z.mp3"}' --language-code en-IN`

# boto3 is not supported for streaming

use `pip3 install amazon-transcribe` instead

# audio formats supported for streaming

- OGG OPUS
- FLAC
- PCM (16 bit little endian minus WAV)

https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html
```
```

# check audio sample hertz and codec

`ffprobe myfile.ogg`
