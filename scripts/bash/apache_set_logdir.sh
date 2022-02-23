#!/bin/bash

for i in $(grep -r "\${APACHE_LOG_DIR}" | sed -r "s/^(.+):.+/\1/"); do echo $i; sudo sed -r 's/\$\{APACHE_LOG_DIR\}/\/home\/a2\/logdir/g' -i $i; done
