import urllib.request
import json

# Define the URL
url = 'http://localhost:11434/api/chat'

article = open("article.txt","r").read()
print(article)
# Define the data payload
data = {
    "model": "mistral",
    "messages": [
        {"role": "user", "content": "this is a scraped article. remove all text that is unrelated to the main article and rewrite this only the relevant lines from this text :\n\n\n ARTICLE: ```" + article + "```"}
    ],
    "options": {
        "temperature": 0
    },
    "stream": False
}

# Convert data to JSON format
data_json = json.dumps(data).encode('utf-8')

# Prepare the request
req = urllib.request.Request(url, data=data_json, headers={'Content-Type': 'application/json'})

# Send the request and print the response
try:
    with urllib.request.urlopen(req) as f:
        response = f.read()
        print(response.decode('utf-8'))
except urllib.error.HTTPError as e:
    print('HTTP Error:', e.code, e.reason)
except urllib.error.URLError as e:
    print('URL Error:', e.reason)
