#!/bin/bash
g1="$1"

if [ ! -r requirements.txt ]; then
	echo generating requirements.txt
else
	echo requirements.txt exists
	exit;
fi

if [ ! -d venv ]; then
	virtualenv venv;
fi

source venv/bin/activate

function add(){
	pip3 install $1
}

function generate(){
	pip3 freeze > requirements.txt
	if [ "$g1" = "-i" ]; then
		echo leaving venv/
	else
		echo removing venv/
		rm -rf venv/
	fi
}

add flask
generate

