#!/bin/bash

function a(){
	export PATH="/abxy:$PATH"
}

function b(){
	echo path is $PATH
}

b;
a;
b;
