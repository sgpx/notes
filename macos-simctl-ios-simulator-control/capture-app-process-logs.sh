#!/bin/bash
sim_id="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
app_identifier="com.myApp.identifier"
cmd_output=$(xcrun simctl launch $sim_id $app_identifier --terminate-running-process)
app_pid=$(echo $cmd_output | sed -r "s/.+\: +([0-9]+)/\1/")
echo pid is $app_pid
echo starting logging...
xcrun simctl spawn booted log stream  --level="debug" --process $app_pid | tee log_$app_pid.txt

