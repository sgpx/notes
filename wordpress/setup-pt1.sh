sudo apt update
sudo apt install apache2 \
                 ghostscript \
                 libapache2-mod-php \
                 mysql-server \
                 php \
                 php-bcmath \
                 php-curl \
                 php-imagick \
                 php-intl \
                 php-json \
                 php-mbstring \
                 php-mysql \
                 php-xml \
                 php-zip

sudo mkdir -p /srv/www
sudo chown www-data: /srv/www
curl https://wordpress.org/latest.tar.gz | sudo -u www-data tar zx -C /srv/www

sudo echo "<VirtualHost *:80>
    DocumentRoot /srv/www/wordpress
    <Directory /srv/www/wordpress>
        Options FollowSymLinks
        AllowOverride Limit Options FileInfo
        DirectoryIndex index.php
        Require all granted
    </Directory>
    <Directory /srv/www/wordpress/wp-content>
        Options FollowSymLinks
        Require all granted
    </Directory>
</VirtualHost>" > tmp.conf

sudo mv tmp.conf /etc/apache2/sites-available/wordpress.conf

sudo a2ensite wordpress

sudo systemctl reload apache2

sudo a2enmod rewrite

sudo systemctl reload apache2

sudo a2dissite 000-default

sudo systemctl reload apache2

echo '


CREATE DATABASE wordpress;


CREATE USER 'wordpress'@'localhost' IDENTIFIED BY 'wordpress';


GRANT ALL PRIVILEGES ON wordpress.* TO 'wordpress'@'localhost';


FLUSH PRIVILEGES; ' > tmp.sql

sudo mysql -u root < tmp.tsql > dbout.txt

cat dbout.txt
