#!/bin/bash
cat -n /usr/share/dict/words | grep -E "^ *$RANDOM\t";
