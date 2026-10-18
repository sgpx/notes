```
from twilio_config import *
from twilio.rest import Client
client = Client(account_sid, auth_token)
q = list(client.messages.stream())
for i in q: 
	print(i.status)
	print(i.date_created)
	print(i.date_sent)
	print(i.to)
	print(i.body)
	print("===")
```
