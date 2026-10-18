# example

standard voice

```
polly_response = polly_client.start_speech_synthesis_task(
        Engine="standard",
        LanguageCode="en-IN",
        OutputFormat="mp3",
        OutputS3BucketName="mybucket",
        Text="The quick brown fox jumps over the lazy dog",
        VoiceId="Aditi",
)
```

neural voice (more expensive)

```
polly_response = polly_client.start_speech_synthesis_task(
        Engine="neural",
        LanguageCode="en-IN",
        OutputFormat="mp3",
        OutputS3BucketName="mybucket",
        Text="The quick brown fox jumps over the lazy dog",
        VoiceId="Kajal",
)
```

# status

```
	task_id = polly_response.get("SynthesisTask").get("TaskId")
        polly_job_data = polly_client.get_speech_synthesis_task(TaskId=task_id)
        pstat = polly_job_data.get("SynthesisTask", {}).get("TaskStatus")
        if pstat == "completed":
            output_uri = polly_job_data.get("SynthesisTask", {}).get("OutputUri")
```
