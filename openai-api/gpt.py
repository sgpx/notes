from openai import OpenAI
from os import getenv


def invoke(prompt, model="gpt-4o", temperature=0):
    if not getenv("OPENAI_API_KEY"):
        raise Exception("openai api key not found")
    client = OpenAI()
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=temperature,
    )
    return completion.choices[0].message.content

def converse(messages=[], model="gpt-4o", temperature=0):
    if not getenv("OPENAI_API_KEY"):
        raise Exception("openai api key not found")
    client = OpenAI()
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return completion.choices[0].message.content