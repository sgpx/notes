#!/bin/bash
a=$(aws polly start-speech-synthesis-task --language-code en-IN --output-format mp3 --output-s3-bucket-name mybucket --text "$1" --voice-id "Kajal" --engine neural | jq 'SynthesisTask.OutputUri')

echo $a

sleep 5

wget $a -O output.mp3

if [ "$(uname -s)" = "Darwin" ]; then
	open output.mp3
else
	xdg-open output.mp3
fi
