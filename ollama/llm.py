from ollama import chat
from ollama import ChatResponse

def invoke(model: str, prompt: str) -> str:
    response: ChatResponse = chat(model=model, messages=[
        {
            'role': 'user',
            'content': user_message,
        },
    ])
    return response['message']['content']
