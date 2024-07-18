#!/bin/bash
docker run -d -p 27017:27017 --name mongodb_container -e MONGO_INITDB_ROOT_USERNAME=myusername -e MONGO_INITDB_ROOT_PASSWORD=mypassword mongo
