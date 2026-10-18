# AWS CLI

## translate text

```
$ aws translate translate-text --text "hello" --source-language-code en --target-language-code es
{
    "TranslatedText": "hola",
    "SourceLanguageCode": "en",
    "TargetLanguageCode": "es"
}
```

## translate document

aws translate translate-document --document '{"ContentType":"text/plain"}'  --source-language-code en --target-language-code hi --document-content fileb://input.txt | jq -r '.TranslatedDocument.Content' | base64 -d
