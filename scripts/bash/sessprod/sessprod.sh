#!/bin/bash
time_input=$(grep -E "^[0-9]+[h|m]$" <<< "$1")
pscore=$(grep -E "^[0-9]+" <<< "$2")
if [ "$time_input" = "" ] || [ "$pscore" = "" ]; then echo Invalid args; exit; fi
xstr=$(sed -r "s/^([0-9]+)([h|m])$/\1_\2/" <<< "$time_input")

echo blah: $xstr

IFS="_" read -ra tm <<< "$xstr"
echo tm0 ${tm[0]}
echo tm1 ${tm[1]}


if [ "${tm[1]}" = "h" ]; then multiplier=3600; else multiplier=60; fi

ctime=$(date +%s)

diff=$(expr "$multiplier" "*" "${tm[0]}")
stime=$(expr "$ctime" '-' "$diff")

platform=$(uname -s)
echo Platform is $platform

if [ platform = "Darwin" ]; then
	dstime=$(date -r $stime)
	dctime=$(date -r $ctime)
else
	dstime=$(date -d "@$stime")
	dctime=$(date -d "@$ctime")
fi

echo $stime
echo Session Start Time: $dstime

echo $ctime
echo Session End Time: $dctime

echo Score: $pscore
echo Message: $3

echo $(uname -s),$stime,$ctime,$pscore,$3 > s.log
