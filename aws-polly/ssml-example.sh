#!/bin/bash
ssml='<speak>
    <prosody rate="fast">
        <say-as interpret-as="words">
            Hi Jim, how can I help you?
        </say-as>
    </prosody>
</speak>'
ssml='<speak>
    Hi Jim, <prosody rate="medium">how can I help you?</prosody>
</speak>'
aws polly synthesize-speech \
--text-type ssml \
--text "$ssml" \
--output-format mp3 \
--voice-id Joanna \
speech.mp3
