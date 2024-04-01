#!/bin/bash
CONTAINER_NAME="mysql_container"
MYSQL_ROOT_PASSWORD="your_root_password"
MYSQL_DATABASE="your_database"
MYSQL_USER="your_username"
MYSQL_PASSWORD="your_password"

if [ "$1" = "--shell" ]; then
  pbcopy <<< "$MYSQL_ROOT_PASSWORD"
  docker exec -it $CONTAINER_NAME mysql -u root --database $MYSQL_DATABASE -p
  exit
fi


# Run MySQL Docker container
docker run -d \
  --name $CONTAINER_NAME \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD \
  -e MYSQL_DATABASE=$MYSQL_DATABASE \
  -e MYSQL_USER=$MYSQL_USER \
  -e MYSQL_PASSWORD=$MYSQL_PASSWORD \
  mysql:latest

# Check if the container is running
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "MySQL container '$CONTAINER_NAME' is running."
else
    echo "Failed to start MySQL container '$CONTAINER_NAME'."
fi
