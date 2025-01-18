#!/bin/bash
if [ -r .env ]; then
	cat ~/prog/notes/postgresql/dbtool/sample.env >> .env
else
	cp -v ~/prog/notes/postgresql/dbtool/sample.env .env
fi


cp -v ~/prog/notes/postgresql/dbtool/db.sh .

cp -v ~/prog/notes/postgresql/dbtool/setup.sql .


dbx="$1"

sed -i.bak -r "s/mystuff/$dbx/g" db.sh
sed -i.bak -r "s/mystuff/$dbx/g" .env
sed -i.bak -r "s/mystuff/$dbx/g" setup.sql

rm *.bak

cat .env
