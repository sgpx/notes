<?php

require_once "vendor/rmccue/requests/src/Autoload.php";
WpOrg\Requests\Autoload::register();
$req = WpOrg\Requests\Requests::get("https://start.fehub.com/eula.html");

$status_code = $req->status_code;

if( $status_code == 200 ){
	print_r("OK\n");
}
else {
	print_r("NOT OK $status_code\n");
}
