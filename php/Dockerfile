FROM php:8.1-apache
RUN rm -rf /var/www/html
RUN apt-get update && apt-get install -y libpng-dev libjpeg-dev libfreetype6-dev && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install gd mysqli pdo pdo_mysql
COPY ./container_source /var/www/html
RUN chown -R www-data:www-data /var/www/html
RUN chmod -R +x /var/www/html
WORKDIR /root
EXPOSE 80
