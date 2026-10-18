#!/bin/bash
if [ "$1" = "--clean" ]; then
	docker stop $(docker ps -aq)
	docker rm $(docker ps -aq)
fi

docker run -d -p 27017:27017 --name foobar_mongodb -e MONGO_INITDB_ROOT_USERNAME=foobar -e MONGO_INITDB_ROOT_PASSWORD=foobar mongo
