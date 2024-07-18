#!/bin/bash
sudo docker exec -it mongodb_container  rm -rfv dump

sudo docker exec -it mongodb_container  mongodump mongodb://foo:foo@localhost:27017/?authSource=admin

sudo docker exec -it mongodb_container  tar cvzf a.tgz dump/
fn="dump-$(date +%s).tgz"

sudo docker exec -it mongodb_container  cat a.tgz > $fn
file $fn
