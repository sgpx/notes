import os
from openai import OpenAI

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OpenAI API Key Not Loaded")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024",
    )
    return response.data[0].url

if __name__ == "__main__":
    print(generate_image("logo for a website"))
