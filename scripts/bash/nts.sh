#!/bin/bash
dn="new-typescript-project"
if [ "$1" != "" ]; then dn="$1"; fi
mkdir -p $dn
cd $dn
yarn init --yes
yarn add typescript ts-node tslib @types/node
yarn run ts-node --eval "console.log(\"done\")"
