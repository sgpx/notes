#!/usr/bin/env python3
import flask

app = flask.Flask(__name__)

@app.route("/",methods=["GET","POST"])
def root():
	return f"Received request : {flask.request.method}",200	
