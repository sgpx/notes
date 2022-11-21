#!/bin/bash
curl -v "$1" -H "Content-Type: application/json" -d "$2"
