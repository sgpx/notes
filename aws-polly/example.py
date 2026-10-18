import boto3

polly_client = boto3.client('polly')
polly_response = polly_client.start_speech_synthesis_task(
        Engine="neural",
        LanguageCode="en-IN",
        OutputFormat="mp3",
        OutputS3BucketName="mybucket-data",
        Text="Hi I am Kajal! Nice to meet you",
        VoiceId="Kajal",
)
