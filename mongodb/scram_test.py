import pymongo

def main():
        client = pymongo.MongoClient("mongodb://myUser:myPwd@0.0.0.0:5000/mydb")
        print(client.mydb.list_collection_names())

main()
