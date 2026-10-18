#!/bin/bash
container_name=myctr
image_name=myimage

function stop_containers(){
	for i in $(docker ps -aq); do
		echo stopping $i;
		docker stop $i;
		docker rm $i;
	done

}

function clean_images() {
	for i in $(docker images --format json | jq -r '.Repository'); do
		echo removing image $i;
		docker rmi $i;
	done

}

if [ "$1" = "--clean" ]; then
	stop_containers;
	clean_images;
fi

a=$(docker images --format json | jq -r '.Repository' | grep $image_name)

if [ "$a" = "" ]; then
	docker build . -t $image_name
fi

docker run --name $container_name -d -p 3000:3000 $image_name bash
sleep 5
curl -v http://localhost:3000
#docker exec -it $container_name bash
printf "\n\n"
