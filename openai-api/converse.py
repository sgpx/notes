from openai import OpenAI
from os import getenv, environ

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


conv_messages = []


while True:
        x = input(">>> ")
        conv_messages.append({"role":"user","content":x})
        resp = get_model_response(messages=conv_messages)
        print("response:\n", resp)
        conv_messages.append({"role":"assistant","content":resp})
