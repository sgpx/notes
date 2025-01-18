import boto3
import json
from base64 import b64decode
from uuid import uuid4

def create_titan_image_prompt(text):
    pbody = {
        "taskType": "TEXT_IMAGE",
        "textToImageParams": {
            "text": text,      
        },
        "imageGenerationConfig": {
            "numberOfImages": 3,
            "height": 768,
            "width": 1152,
            "cfgScale": 8,
            "seed": 0
        }
    }
    return json.dumps(pbody)

def generate_images(text: str):
    s3 = boto3.client("s3")
    bedrock = boto3.client("bedrock-runtime")
    prompt = create_titan_image_prompt(text=text)
    res = bedrock.invoke_model(
        body=prompt.encode("utf-8"), modelId="amazon.titan-image-generator-v1", accept="application/json", contentType="application/json"
    )
    raw_response = res["body"].read().decode("utf-8")
    jdata = json.loads(raw_response)
    images = jdata.get("images")
    imagepaths = []
    for i in images:
        file_bytes = b64decode(i)
        file_name = f"{str(uuid4())}.jpg"
        local_file_path = f"/tmp/{file_name}"
        open(local_file_path, "wb").write(file_bytes)
        s3.upload_file(local_file_path, aws_bucket_id, file_name)
        imgsrc = f"https://{aws_bucket_id}.s3.amazonaws.com/{file_name}"
        imagepaths.append(imgsrc)
    return imagepaths

if __name__ == "__main__":
    import sys
    generate_images(sys.argv[-1])
