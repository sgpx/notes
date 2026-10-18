#!/bin/bash

ENV_FILE=".env"

# Create .env file with sample values if it does not exist
if [ ! -f "$ENV_FILE" ]; then
  cat > "$ENV_FILE" <<EOF
POSTGRES_USER=sample123
POSTGRES_PASSWORD=sample123
POSTGRES_DB=sample123
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
EOF
  echo "$ENV_FILE file created with sample values. Please review and update as needed."
fi

# Load environment variables from .env
source "$ENV_FILE"

platform=$(uname -s)
export PGPASSWORD="$POSTGRES_PASSWORD"
DOCKER_IMAGE="postgres:latest"
CONTAINER_NAME="mystuff_postgres"

function db_setup() {
  docker cp setup.sql $CONTAINER_NAME:/root/setup.sql
  docker exec $CONTAINER_NAME psql -h $POSTGRES_HOST -U $POSTGRES_USER -f /root/setup.sql -d $POSTGRES_DB
}

if [ "$platform" = "Darwin" ]; then
  open -a Docker.app
  echo "waiting for docker to start"
  while [ "$(pgrep com.docker)" = "" ]; do
    sleep 1
  done
fi

if [[ "$1" = "--reset" ]]; then
  docker exec $CONTAINER_NAME dropdb -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER --no-password --if-exists $POSTGRES_DB
  docker exec $CONTAINER_NAME createdb -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER --no-password $POSTGRES_DB 
  db_setup
  exit
fi

if [[ "$1" = "--dump" ]]; then
  fn="dump-$POSTGRES_DB-$(date +%s).sql"
  docker exec -it -e PGPASSWORD="$POSTGRES_PASSWORD" $CONTAINER_NAME pg_dump -h "127.0.0.1" -p 5432 -U $POSTGRES_USER -d $POSTGRES_DB -Fp > $fn
  exit
fi

if [[ "$1" = "--pg" || "$1" = "--pgshell" ]]; then
  docker exec -it -e PGPASSWORD="$POSTGRES_PASSWORD" $CONTAINER_NAME psql -h "127.0.0.1" -p 5432 -U $POSTGRES_USER -d $POSTGRES_DB --no-password
  exit
fi

if [ "$1" = "--shell" ]; then
  docker exec -it $CONTAINER_NAME bash
  exit
fi

if [ "$1" = "--clean" ]; then
  docker stop $CONTAINER_NAME
  docker rm $CONTAINER_NAME
  exit
fi

docker run -d \
  --name $CONTAINER_NAME \
  -p $POSTGRES_PORT:5432 \
  -e POSTGRES_USER=$POSTGRES_USER \
  -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
  -e POSTGRES_DB=$POSTGRES_DB \
  $DOCKER_IMAGE

sleep 5
db_setup

echo "PostgreSQL container is running on port $POSTGRES_PORT."
echo "Container name: $CONTAINER_NAME"
echo "Username: $POSTGRES_USER"
echo "Password: $POSTGRES_PASSWORD"
echo "Database name: $POSTGRES_DB"