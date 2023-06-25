#!/bin/bash
for i in {0..10}; do
	y=$(aws amplify list-apps | jq ".apps[$i]")
	echo $y
	domain=$(echo $y | jq -r '.defaultDomain')
	branchName=$(echo $y | jq -r '.productionBranch.branchName')
	echo $branchName.$domain
	echo "    "
done
