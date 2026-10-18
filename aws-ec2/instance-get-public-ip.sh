#!/bin/bash
bash get-public-ips-for-all-instances.sh | grep "$1" | sed -r "s/(.+) # (.+) # (.+)/\2/g" | head -n1
