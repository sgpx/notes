from openai import OpenAI
from os import getenv, environ
import base64

environ["OPENAI_API_KEY"] = open("apikey.txt","r").read().strip()



def get_model_response(model="gpt-4o", messages = []):
    if not getenv("OPENAI_API_KEY"):
        raise Exception("openai api key not found")
    client = OpenAI()
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=1,
    )
    return completion.choices[0].message.content


g_messages = []


while True:
        x = input(">>> ")
        if x[:4] == "exit": exit(0)
        if x == "!img":
            imglink = input("enter image link: ")
            x = input("enter text: ")
            g_messages.append({"role":"user","content": [{"type":"text","text":x}, {"type":"image_url","image_url": {"url": "data:image/jpg;base64,"  + base64.b64encode(open(imglink,"rb").read()).decode("utf-8") }}]})
        else:
            g_messages.append({"role":"user","content":x})
        resp = get_model_response(messages=g_messages)
        print("response:\n", resp)
        g_messages.append({"role":"assistant","content":resp})
