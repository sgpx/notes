#!/bin/bash
echo enter password
read pwd

db_name="mydb"

if [ "$1" != "" ]; then
	db_name="$1"
fi

function dump_table() {
	table_name="$1";
	fn="$table_name-dump.sql";
	2>/dev/null mysqldump $db_name $table_name --password="$pwd" --user myuser --compact --result-file $fn;
}


fl="dump-$(date +%s)"
mkdir $fl
cd $fl
pwd

IFS=$'\n'
a=$(mysql --user myuser --password="$pwd" --execute="show tables;" --batch mydb)
ctr=0

for i in $a; do
	if [ $ctr -eq 0 ]; then
		ctr=1; 
	else
		echo dumping $i;
		dump_table $i; 
	fi; 
done

zip -r $HOME/$fl.zip .
echo $HOME/$fl.zip
