# install

`apt install -y php`

# php interactive shell

`php -a`

# start built in web server

`php -S localhost:8080 --docroot /foo/bar`

# SimpleXMLElement not found error

`apt install -y php$php_version-xml`

e.g. `apt install -y php7.4-xml`

# arrays

actually an ordered map

```
<?php

$a = array("hey" => "ya");
echo $a["hey"];
```

without keys


```
<?php

$a = array(1,2,3,4);
echo $a[0];
```

# `print_r`

display human readable info about any variable

# `$_SERVER`

superglobal variable 

holds info about headers, paths, locations, etc

```
<?php
echo $_SERVER["QUERY_STRING"]';
echo $_SERVER["REQUEST_METHOD"];

```

# `$_REQUEST`

associative array

contains `$_GET`, `$_POST`, `$_COOKIE`

# `$_POST`

contains info about post request

passed to the current script via the HTTP POST method when using `application/x-www-form-urlencoded` or `multipart/form-data`

# `php://input` 

`php://input` is a read-only stream that allows you to read raw data from the request body

# read json from post request

```
<?php
$json = file_get_contents('php://input');

$data = json_decode($json);
?>
```

# `gettype()`

# get all methods of a class/object : `get_class_methods()`

```
use Aws\Sdk;

$sharedConfig = [
    'profile' => 'default',
    'region' => 'us-east-1',
    'version' => 'latest'
];

$sdk = new Aws\Sdk($sharedConfig);

$s3Client = $sdk->createS3();
print_r(get_class_methods($s3Client));
```

# get_object_vars()

```
$name = get_object_vars(json_decode("php://input"))["name"];
```
