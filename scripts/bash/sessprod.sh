#!/bin/bash
time_input=$(grep -E "^[0-9]{1,2}[h|m]$" <<< "$1")
pscore=$(grep -E "^[0-9]{1,2}" <<< "$2")
if [ "$time_input" = "" ] || [ "$pscore" = "" ]; then echo Invalid args; exit; fi
IFS="_" read -a tm <<< $(sed -r "s/^([0-9]{1,2})([h|m])$/\1_\2/" <<< "$time_input")

if [ "${tm[1]}" = "h" ]; then multiplier=3600; else multiplier=60; fi

ctime=$(date +%s)

diff=$(expr "$multiplier" "*" "${tm[0]}")
stime=$(expr "$ctime" '-' "$diff")


echo Platform is $(uname -s)

echo $stime
echo Session Start Time: $(date -d "@$stime")

echo $ctime
echo Session End Time: $(date -d "@$stime")

echo Score: $pscore

echo $(uname -s),$stime,$ctime,$pscore
