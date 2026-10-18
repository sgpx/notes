# python

`pip3 install python-dotenv`

# example

```
import os
import dotenv
env_loaded = dotenv.load_dotenv(".env")
print(env_loaded)
print(os.environ["DB_URL"])
```
