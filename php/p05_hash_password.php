<?php

$pw = "foobar";
$salt = random_bytes(64);
$algorithm = "sha512";
$hpw = hash_pbkdf2($algorithm, $pw, $salt, 10);
print_r($hpw);
