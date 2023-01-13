<?php

function foobar(string $x)
{
    $a = "";
    for($i = 0; $i < strlen($x); $i++){
        if(ctype_alnum($x[$i])) $a .= $i;
    }
    return $a;
}

print_r(foobar("abcdef"));

?>
