# composer

php package manager

# setup (v2)

```
apt install -y php
wget -v https://getcomposer.org/installer
php installer
echo #!/bin/bash > /usr/bin/composer
echo COMPOSER_ALLOW_SUPERUSER=1 /root/composer.phar \$@ >> /usr/bin/composer
```

# setup (ubuntu)

`apt install -y composer`

# package registry

packagist.com

# init (v1)

`composer init --quiet` 

or 

`composer init -q`

# init (v2)

`composer init --name myname/mypackage -q`

# install package

`composer require rmccue/requests`

# invoke package

`require "/path/to/vendor/mypackage/foo.php"`

`include "/path/to/vendor/mypackage/foo.php"`

`require_once "/path/to/vendor/mypackage/foo.php"`

