import anthropic
import os
from typing import List, Dict, Any

def converse(messages: List[Dict[str, Any]] = None, 
             model: str = "claude-opus-4-6",
             temperature: float = 1.0,
             max_tokens: int = 4096) -> str:
    """Send conversation messages to Claude 4.6 Opus."""
    if messages is None:
        messages = []
    
    client = anthropic.Anthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )
    
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=messages
    )
    
    return response.content[0].text

def invoke(prompt: str = "", 
           model: str = "claude-opus-4-6",
           temperature: float = 1.0,
           max_tokens: int = 4096) -> str:
    """Send a single prompt to Claude 4.6 Opus."""
    client = anthropic.Anthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )
    
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.content[0].text

if __name__ == "__main__":
    print(invoke(prompt="What should I learn after CIFARNet in Pytorch?"))
