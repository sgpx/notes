#!/bin/bash
a=$(ls *.java | sort -n | tail -n1)
nano $a
