#!/bin/bash
cargo run
if [ "$?" != "0" ]; then
	exit
fi

a=$(ls arch/*.rs | sort -n | tail -n1)

if [ "$a" = "" ]; then
	d="arch/u01.rs"
else
	b=$(sed -r "s/arch\/u([0-9]+).rs/\1/" <<<"$a")
	c=$(expr $b '+' 1)
	d=$(printf "arch/u%02d.rs" $c)
	if [ "$(diff src/main.rs $a)" = "" ]; then echo not copying..; exit; fi
fi

rustfmt src/main.rs
cp -v src/main.rs $d
