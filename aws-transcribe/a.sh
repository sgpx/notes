#!/bin/bash
mybucket="blah123"
job_id="tj-$(python3 -m uuid)"
echo creating job $job_id
nfn="s3://$job_id/transcribe-test/$1"
aws s3 cp $1 $nfn
aws transcribe start-transcription-job --region ap-south-1 --transcription-job-name $job_id --media "{\"MediaFileUri\":\"$nfn\"}" --language-code en-IN
curl "$(aws transcribe get-transcription-job --transcription-job-name $job_id | jq -r '.TranscriptionJob.Transcript.TranscriptFileUri')" | jq '.' a.json
