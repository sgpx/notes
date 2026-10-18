<?php
$a = [array("a" => "b", "c" => "d"), array("c" => "bbbbddd")];
$z=[];foreach($a as $i){ foreach($i as $j => $k) $i[$j] = str_replace("b", "x", $k); array_push($z, $i); };
print_r($z);
?>
