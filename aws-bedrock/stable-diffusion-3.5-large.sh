# echo '{"steps":25, prompt":"a beautiful night sky in colorado woods")' | base64 > prompt.json
prompt=$(gpt4.sh -p "enhance this prompt for DALL-E. make it more descriptive and visual: $1")
prompt=$(echo $prompt | sed -r 's/"//g')
echo "{\"prompt\":\"$prompt\",\"mode\":\"text-to-image\",\"aspect_ratio\":\"1:1\",\"output_format\":\"png\",\"seed\":0}" | base64 > prompt.json

aws bedrock-runtime invoke-model \
  --model-id stability.sd3-5-large-v1:0 \
  --body file://prompt.json \
  --region us-west-2 \
  output.json

jq -r '.images[0]' output.json > o.base64
base64 -d -i o.base64 -o a.png
open a.png
