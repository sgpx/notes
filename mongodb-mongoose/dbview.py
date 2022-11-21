#!/usr/bin/env python3
from pymongo import MongoClient as mc
dbname = "testdb"
colname = "pets"

from sys import argv, exit
print("argc:", len(argv), argv)
if len(argv) == 3:
	[_, dbname, colname] = argv
elif len(argv) == 2:
	colname = argv[-1]


a = f"mongodb://localhost:5000/{dbname}"
b = mc(a)
c = b[dbname]
print(c.list_collection_names())

d = c[colname]

for i in d.find():
	print(i)
