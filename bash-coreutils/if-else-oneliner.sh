#!/bin/bash
a=$(ls | wc -l | sed -r "s/ +//");
if [ "$a" = "1" ]; then echo yes; else echo no; fi
