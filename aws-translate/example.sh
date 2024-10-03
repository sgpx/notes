#!/bin/bash
aws translate translate-document --document '{"ContentType":"text/plain"}'  --source-language-code en --target-language-code hi --document-content fileb://input.txt | jq -r '.TranslatedDocument.Content' | base64 -d
