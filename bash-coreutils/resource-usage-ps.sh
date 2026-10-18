#!/bin/bash
date -Iseconds > $HOME/memcpu.out
ps -eo pid,user,args,%mem,%cpu --sort=-%cpu >> $HOME/memcpu.out
