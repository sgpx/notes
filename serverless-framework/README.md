# REMINDER: SERVERLESS FRAMEWORK IS PAID NOW, DO NOT USE

# python3.9 ENOENT error in ubuntu

`sudo apt install -y python3.9`

# set OS environment variables in serverless.yml

set

```
provider:
  name: aws
  runtime: python3.9
  stage: dev
  region: us-east-1
  environment:
    MYSECRET: foobar
```

access

```
import flask
import os

app = flask.Flask(__name__)

@app.route('/')
def index():
    return repr(os.environ.get("MYSECRET")), 200
```


# deploy app

`sls deploy`

# get information about app

```
$ sls info

Service Information
service: foobar-app-1
stage: dev
region: us-east-1
stack: foobar-app-1-dev
resources: 12
api keys:
  None
endpoints:
  ANY - https://foobar.execute-api.us-east-1.amazonaws.com/dev
functions:
  app: foobar-app-1-dev-app
layers:
  None
```

# setup (python/flask)

`yarn init --yes && yarn add serverless-wsgi serverless-python-requirements`

# setup (nodejs/expresjs)

`yarn init --yes && yarn add express serverless-http`
