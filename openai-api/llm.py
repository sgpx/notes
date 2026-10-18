import dotenv
dotenv.load_dotenv(override=True)

import os

from openai import OpenAI

DEFAULT_MODEL = "gpt-5.4-mini"
EMBEDDING_MODEL = "text-embedding-3-small"
HARD_TRUNCATE_LIMIT = 700_000

client = OpenAI()


def converse(messages: list, model: str = DEFAULT_MODEL, temperature: float = 1.0) -> str:
    response = client.chat.completions.create(
        messages=messages,
        temperature=temperature,
        model=model,
    )
    return response.choices[0].message.content


def invoke(user_message: str, reasoning_effort : str = "low") -> str:
    #print("invoke called")
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message[:HARD_TRUNCATE_LIMIT],
            },
        ],
        temperature=1.0,
        model=DEFAULT_MODEL,
        reasoning_effort=reasoning_effort
    )
    return response.choices[0].message.content

def get_embedding(text: str) -> list[float]:
    print("get_embedding called")
    text = text.replace("\n", " ")
    resp = client.embeddings.create(input=[text], model=EMBEDDING_MODEL)
    return resp.data[0].embedding
