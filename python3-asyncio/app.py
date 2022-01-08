import flask
import time
import asyncio

app = flask.Flask(__name__)

async def foo():
	time.sleep(10)
	a = open("a.txt","r").read()+"1"
	open("a.txt","w").write(a)

@app.route("/")
def index():
	asyncio.run(foo())
	return "OK",200
