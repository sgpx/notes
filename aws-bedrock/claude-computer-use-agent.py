import base64
import json
import boto3
import time
import pyautogui
import os
from uuid import uuid4

v4 = lambda: str(uuid4())

apibody = lambda msgs: {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 512,
    "temperature": 0.5,
    "messages": msgs,
    "tools": [
        {  # new
            "type": "computer_20241022",  # literal / constant
            "name": "computer",  # literal / constant
            "display_height_px": 1440,  # min=1, no max
            "display_width_px": 900,  # min=1, no max
            "display_number": 0,  # min=0, max=N, default=None
        },
        {  # new
            "type": "bash_20241022",  # literal / constant
            "name": "bash",  # literal / constant
        },
        {  # new
            "type": "text_editor_20241022",  # literal / constant
            "name": "str_replace_editor",  # literal / constant
        },
    ],
    "anthropic_beta": ["computer-use-2024-10-22"],
}


def execute_tool(data):
    # Extract the tool use information
    if len([i for i in data.get("content") if i.get("type") == "tool_use"]) == 0:
        exit(0)
    tool_use = next(
        (item for item in data["content"] if item["type"] == "tool_use"), None
    )

    if (
        tool_use
        and tool_use["name"] == "computer"
        and tool_use["input"]["action"] == "mouse_move"
    ):
        # Extract the coordinates
        x, y = tool_use["input"]["coordinate"]

        # Perform the mouse movement
        pyautogui.moveTo(x, y+10)
        return {
            "content": f"Mouse moved to coordinates: ({x}, {y})",
            "tool_use_id": tool_use["id"],
        }
    elif (
        tool_use
        and tool_use["name"] == "computer"
        and tool_use["input"]["action"] == "left_click"
    ):
        # Perform the mouse movement
        pyautogui.click()
        return {"content": f"Mouse clicked", "tool_use_id": tool_use["id"]}
    elif (
        tool_use
        and tool_use["name"] == "computer"
        and tool_use["input"]["action"] == "screenshot"
    ):
        # Perform the mouse movement
        #pyautogui.click()
        return {"content": f"Screenshot taken", "tool_use_id": tool_use["id"]}
    elif (
        tool_use
        and tool_use["name"] == "computer"
        and tool_use["input"]["action"] == "type"
    ):
        # Ensure the 'text' key exists in input
        text_to_type = tool_use["input"].get("text", "")
        if text_to_type:
            pyautogui.typewrite(text_to_type)
            return {
                "content": f"Text '{text_to_type}' typed",
                "tool_use_id": tool_use["id"],
            }
        else:
            return {
                "content": "No text provided to type",
                "tool_use_id": tool_use["id"],
            }
    elif (
        tool_use
        and tool_use["name"] == "computer"
        and tool_use["input"]["action"] == "key"
    ):
        # Ensure the 'key' key exists in input
        key_to_press = tool_use["input"].get("text", "")
        if key_to_press:
            pyautogui.press(key_to_press)
            return {
                "content": f"Key '{key_to_press}' pressed",
                "tool_use_id": tool_use["id"],
            }
        else:
            return {
                "content": "No key provided to press",
                "tool_use_id": tool_use["id"],
            }
    else:
        return {"content": f"Error: Failed", "tool_use_id": tool_use["id"]}


MODEL_ID = "anthropic.claude-3-5-sonnet-20241022-v2:0"


def load_scr():
    imgpath = f"tmp-{v4()}.png"
    pyautogui.screenshot(imgpath).save(imgpath)
    im2 = imgpath.replace(".png","-x.png")
    os.system(f"magick {imgpath} -resize 1440x900 {im2}")
    image_base64 = base64.b64encode(open(im2, "rb").read()).decode("utf-8")
    return image_base64


prompt = "Test my website called foobar at http://localhost:3000/ from a customer POV"
print(prompt)
g_msgs = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/png",
                    "data": load_scr(),
                },
            },
        ],
    }
]

bedrock_runtime = boto3.client(
    "bedrock-runtime",
    region_name="us-west-2",
)

invoke = lambda: json.loads(
    bedrock_runtime.invoke_model(
        modelId=MODEL_ID, body=json.dumps(apibody(msgs=g_msgs))
    )["body"]
    .read()
    .decode("utf-8")
)

time.sleep(2)
ctr = 0
while True:
    print(ctr)
    ctr += 1
    try:
        llm_response = invoke()
    except Exception as e:
        print(e)
        continue
    print(llm_response)
    ltext = [i.get("text") for i in llm_response.get("content") if i.get("type") == "text"]
    print("LLM: " + "\n".join(ltext))
    toolresp = execute_tool(llm_response)
    print(toolresp)
    g_msgs.append(
        {i: llm_response[i] for i in llm_response if i in ["role", "content"]}
    )
    g_msgs.append(
        {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": toolresp.get("tool_use_id"),
                    "content": toolresp.get("content"),
                },
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": load_scr(),
                    },
                },
            ],
        }
    )
    # print(g_msgs)
