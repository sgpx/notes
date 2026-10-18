#!/bin/bash

# input and output paths
input_path="$1"
output_path="$1_output.mp4"
ffmpeg -i "$input_path" -vf "scale=1080:720" -c:v libx264 -crf 23 -c:a aac "$output_path"
