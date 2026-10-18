source .env
curl -v -X POST https://api.openai.com/v1/chat/completions \
     -H "Authorization: Bearer $OPENAI_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
           "model": "gpt-3.5-turbo",
           "messages": [
             {
               "role": "user",
               "content": "Is the earth a planet? Answer in one word YES or NO"
             }
           ]
         }'
