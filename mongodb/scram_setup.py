#!/usr/bin/env python3
import pymongo

def main(db_name="mydb", username="myUser", pwd="myPwd"):
	client = pymongo.MongoClient("mongodb://0.0.0.0:5000")
	print(client.list_database_names())

	db = client[db_name]	
	res = db.command("createUser", username, pwd=pwd, roles=[{"role":"readWrite", "db":db_name}])
	print(res)

if __name__ == "__main__":
	main()
