#!/bin/bash
2>&1 ffprobe $1 | grep Duration: | sed -r "s/Duration: +([0-9\.:]+), start.+/\1/g"
