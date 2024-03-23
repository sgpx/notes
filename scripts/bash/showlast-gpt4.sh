#!/bin/bash
GPT_PATH=$HOME/prog/gpt4
jq -r '.choices[0].message.content' <<< $(cat $(ls $GPT_PATH/response* | sort -n | tail -n1))
