from openai import OpenAI
from os import getenv


def get_model_response(prompt, answer_only=True, model="gpt-3.5-turbo"):
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
        temperature=0,
    )
    if answer_only:
        return completion.choices[0].message.content
    return {"prompt": prompt, "answer": completion.choices[0].message.content}
