# prerequistes

setup aws credentials in `$HOME/.aws/credentials` or in environment variables

# install

```
composer init --name abc/xyz -q
composer require aws/aws-sdk-php
printf "<?php\nrequire 'vendor/autoload.php';\n" > a.php
```

# setup sdk object

```
require "vendor/autoload.php";

use Aws\Sdk;

$sharedConfig = [
    'profile' => 'default',
    'region' => 'us-east-1',
    'version' => 'latest'
];

$sdk = new Aws\Sdk($sharedConfig);
```

# s3 view buckets

```
$s3Client = $sdk->createS3();

print_r($s3Client->listBuckets());
```



