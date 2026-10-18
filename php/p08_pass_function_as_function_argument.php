<?php

function execute($myfunc, $value){
	print_r("executing $myfunc with value $value..\n");
	return $myfunc($value);
}

function double($x){
	return $x * 2;
}

print_r(execute("double", 232));
