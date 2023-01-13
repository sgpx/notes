<?php
echo "Hello World\n";

$a="1";
$b="$a 2\n";

echo $a . "\n";
print_r($b);
fwrite(fopen("php://stdout", "w"), "3\n");
?>
