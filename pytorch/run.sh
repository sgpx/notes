#!/bin/bash
./venv/bin/python3 $(ls *.py | sort -n | tail -n1)
