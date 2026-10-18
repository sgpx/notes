<?php

$servername = "localhost";
$username = "";
$password = "";
$dbname = "db";

$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
} 

$sql = "SHOW DATABASES;";
$result = $conn->query($sql);

print_r($result);

while($row = $result->fetch_assoc()) {
	print_r($row);
}
?>
