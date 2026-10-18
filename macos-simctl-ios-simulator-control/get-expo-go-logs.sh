#!/bin/bash
sim_id="ABC-DEF-GHI-JKL"
app_identifier="host.exp.Exponent"
cmd_output=$(xcrun simctl launch $sim_id host.exp.Exponent --terminate-running-process)
echo $cmd_output
app_pid=$(echo $cmd_output | sed -r "s/.+\: +([0-9]+)/\1/")
echo pid is $app_pid
echo starting logging...
xcrun simctl spawn booted log stream  --level="debug" | grep -i expo
