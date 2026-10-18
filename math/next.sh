#!/bin/bash
cx -z --emit 'what do you think of my progress, along with 5 immediate problems to solve'
printf "\n\nthis is a summary of my practice code" >> ~/Desktop/cx-tmp.txt
cat ~/prog/mluniv/numpy.md >> ~/Desktop/cx-tmp.txt
cat ~/prog/mluniv/pytorch.md >> ~/Desktop/cx-tmp.txt
cat ~/prog/mluniv/cuda.md >> ~/Desktop/cx-tmp.txt
nano ~/Desktop/cx-tmp.txt
nvidia-nemotron-ultra.sh -i ~/Desktop/cx-tmp.txt > ~/tmp.txt
vbx.sh -f ~/tmp.txt
