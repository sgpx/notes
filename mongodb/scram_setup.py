#!/usr/bin/env python3
import pymongo

def setup(db_name="mydb", username="myUser", pwd="myPwd", dbUrl = "mongodb://0.0.0.0:5000/"):
	client = pymongo.MongoClient(dbUrl)
	print(client.list_database_names())

	db = client[db_name]	
	res = db.command("createUser", username, pwd=pwd, roles=[{"role":"readWrite", "db":db_name}])
	print(res)

def test_scram(db_name="mydb", username="myUser", pwd="myPwd", dbUrl = "mongodb://0.0.0.0:5000/"):
	client = pymongo.MongoClient(dbUrl)
	print(client.server_info())
	#print(client.list_database_names())
	#print(client[db_name].list_collection_names())
	import time
	res = client[db_name]["testcol"].insert_one({"a" : "b", "t" : time.time() })
	print(res)
if __name__ == "__main__":
	setup()
