#!/bin/bash

DOCKER_IMAGE="postgres:latest"
CONTAINER_NAME="postgres_container"
POSTGRES_PORT=4001
POSTGRES_USER="username"
POSTGRES_PASSWORD="password"
POSTGRES_DB="xdb"

docker run -d \
  --name $CONTAINER_NAME \
  -p $POSTGRES_PORT:5432 \
  -e POSTGRES_USER=$POSTGRES_USER \
  -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
  -e POSTGRES_DB=$POSTGRES_DB \
  $DOCKER_IMAGE

echo "PostgreSQL container is running on port $POSTGRES_PORT."
echo "Container name: $CONTAINER_NAME"
echo "Username: $POSTGRES_USER"
echo "Password: $POSTGRES_PASSWORD"
echo "Database name: $POSTGRES_DB"

