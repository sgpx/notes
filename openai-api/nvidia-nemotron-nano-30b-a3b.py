#!/usr/bin/python3
from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1", api_key=os.getenv("NVIDIA_API_KEY")
)

THINKING_ENABLED = False


def invoke(prompt: str) -> str:
    completion = client.chat.completions.create(
        model="nvidia/nemotron-3-nano-30b-a3b",
        max_tokens=4000,
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        top_p=0.95,
        extra_body={"chat_template_kwargs": {"thinking": THINKING_ENABLED}},
        stream=False,
    )
    return completion.choices[0].message.content


def converse(messages: List[dict]) -> str:
    completion = client.chat.completions.create(
        model="nvidia/nemotron-3-nano-30b-a3b",
        max_tokens=4000,
        messages=messages,
        temperature=1,
        top_p=0.95,
        extra_body={"chat_template_kwargs": {"thinking": THINKING_ENABLED}},
        stream=False,
    )
    return completion.choices[0].message.content
