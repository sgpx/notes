#!/bin/bash
function main(){
	for i in $(2>/dev/null find . -type d -depth 1);
		do du -hs $i;
	done
}

main | grep -E "^[0-9\.]{3,}(G|M)"
