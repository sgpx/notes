#!/bin/bash
bash get-instance-vpcs.sh | grep "$1" | sed -r "s/(.+) # (.+) # (.+)/\2/g" | head -n1
