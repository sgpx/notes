from ollama import Client
from ollama import ChatResponse


from ollama import Client

allowed_referrer = "http://1.2.3.4:8000"
ollama_api_endpoint = "http://1.2.3.4:11434"
client = Client(host=ollama_api_endpoint, headers={"referrer": allowed_referrer})


chat = client.chat


def invoke(prompt: str = "", model="") -> str:
    response: ChatResponse = chat(
        model="deepseek-r1:8b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    raw_resp = response["message"]["content"]
    return raw_resp.split("</think>").pop() if "</think>" in raw_resp else raw_resp


def converse(messages=[], model="") -> str:
    print(messages)
    response: ChatResponse = chat(model="deepseek-r1:8b", messages=messages)
    raw_resp = response["message"]["content"]
    return raw_resp.split("</think>").pop() if "</think>" in raw_resp else raw_resp
