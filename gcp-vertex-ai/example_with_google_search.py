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
        raise Exception("GOOGLE_API_KEY not found")
    
    return genai.Client(
        api_key=api_key,
        vertexai=True,
    )

def get_config(temperature):
    # This enables the Google Search tool for grounding
    google_search_tool = types.Tool(
        google_search=types.GoogleSearch()
    )
    
    return types.GenerateContentConfig(
        temperature=temperature,
        tools=[google_search_tool]
    )

def invoke(prompt, model="gemini-3-pro-preview", temperature=0):
    debug_log(
        "Invoking Gemini with Search",
        model=model,
        temperature=temperature,
        prompt_preview=prompt[:200],
    )
    
    client = get_client()
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=get_config(temperature)
    )
    
    # Note: response.text will now include grounded information
    content = response.text
    debug_log("LLM response received", model=model, response_preview=content[:200])
    return content

def converse(messages=[], model="gemini-3-pro-preview", temperature=0):
    debug_log(
        "Starting Gemini search-enabled conversation",
        model=model,
        temperature=temperature,
        message_count=len(messages),
    )
    
    client = get_client()
    
    # Format messages: OpenAI 'assistant' -> Gemini 'model'
    formatted_messages = []
    for m in messages:
        role = "model" if m["role"] == "assistant" else m["role"]
        formatted_messages.append({"role": role, "parts": [{"text": m["content"]}]})

    response = client.models.generate_content(
        model=model,
        contents=formatted_messages,
        config=get_config(temperature)
    )
    
    content = response.text
    debug_log("Conversation response received", model=model, response_preview=content[:200])
    return content


print(invoke("what is the difference between keras and pytorch"))
