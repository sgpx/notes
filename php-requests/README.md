# requests

based off python requests

# install

```
composer init --quiet
composer require rmccue/requests
```

# how to use

register autoloader before starting using

`WpOrg\Requests\Autoload::register();`

# demo

```
<?php

require_once "vendor/rmccue/requests/src/Autoload.php";
WpOrg\Requests\Autoload::register();
$req = WpOrg\Requests\Requests::get("https://github.com/");

$status_code = $req->status_code;

if( $status_code == 200 ){
	print_r("OK\n");
}
else {
	print_r("NOT OK $status_code\n");
}
```
