import dotenv
dotenv.load_dotenv()

from google import genai
from google.genai import types
from os import getenv
import json
import datetime

def debug_log(message, **kwargs):
    ts = datetime.datetime.utcnow().isoformat()
    if kwargs:
        try:
            payload = json.dumps(kwargs, default=str)
        except Exception:
            payload = str(kwargs)
        print(f"[LLM DEBUG {ts}] {message} | {payload}")
    else:
        print(f"[LLM DEBUG {ts}] {message}")

def get_client():
    api_key = getenv("GOOGLE_API_KEY")
    if not api_key:
        raise Exception("GOOGLE_API_KEY not found in environment variables")
    
    # Initialize the GenAI client for Vertex AI
    return genai.Client(
        api_key=api_key,
        vertexai=True, 
    )

def invoke(prompt, model="gemini-3-pro-preview", temperature=0):
    debug_log(
        "Invoking Gemini",
        model=model,
        temperature=temperature,
        prompt_preview=prompt[:200],
    )
    
    client = get_client()
    config = types.GenerateContentConfig(temperature=temperature)
    
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=config
    )
    
    content = response.text
    debug_log("LLM response received", model=model, response_preview=content[:200])
    return content

def converse(messages=[], model="gemini-3-pro-preview", temperature=0):
    """
    Note: Gemini expects 'user' and 'model' roles (not 'assistant').
    The 'messages' should be a list of dicts: {'role': 'user/model', 'parts': [{'text': '...'}]}
    """
    debug_log(
        "Starting Gemini conversation",
        model=model,
        temperature=temperature,
        message_count=len(messages),
    )
    
    client = get_client()
    config = types.GenerateContentConfig(temperature=temperature)

    # Vertex AI SDK expects 'contents' as a list of types.Content or dicts
    # We map 'assistant' to 'model' for compatibility with OpenAI-style lists
    formatted_messages = []
    for m in messages:
        role = "model" if m["role"] == "assistant" else m["role"]
        formatted_messages.append({"role": role, "parts": [{"text": m["content"]}]})

    response = client.models.generate_content(
        model=model,
        contents=formatted_messages,
        config=config
    )
    
    content = response.text
    debug_log("Conversation response received", model=model, response_preview=content[:200])
    return content

if __name__ == "__main__":
    a = invoke("what is TF-IDF in neural networks")
    print(a)
