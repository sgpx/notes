<?php

$servername = "localhost";
$username = "";
$password = "";
$dbname = "mydb";

$conn = new mysqli($servername, $username, $password, $dbname);
$sel = $conn->query("show tables;");
print_r($sel);	

$a = $sel->fetch_assoc();
print_r($a);
