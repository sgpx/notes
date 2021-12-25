# dynamodb

# core components

- tables
- items
- attributes

# ...

- table is a collection of items
- item is a collection of attributes

- dynamodb uses primary key to identify each item

# tables

dynamodb stores data in tables

table is a collection of data

# items

each table contains zero or more items

item is a group of attributes

no limit to number of items

# attributes

each item has one or more attributes

each attribute is a fundamental data elemenet

# primary key

when you create a table, you must specify the primary key of the table

primary key uniquely identifies each item in the table

no two items can have same key

# types of primary key

- partition key: simple primary key with one attribute known as partition key

- partition key and sort key: two attributes, first is partion key and second is sort key

# =================

Keys can be composed of one attribute, called a hash key, or a compound key called the hash and range key

A Hash Key consists of a single attribute that uniquely identifies an item.

A Hash and Range Key consists of two attributes that together, uniquely identify an item.

# =================

partition key is used as internal hash

output from hash function determines partition in which item is stored

all items with same partition key value are stored together, in sorted order by sort key value

in table with partion key + sort key, it is possible for items to have same partition key (but they must have different sort keys)

secondary index lets you query the data in the table using an alternate key, in addition to queries against the primary key

# dynamodb API operations

# control plane

create and manage dynamodb tables

- CreateTable = creates a new table

- DescribeTable = returns info about table

- ListTables = returns all table names in a list

- UpdateTable = modifies settings of table or its indexes

- DeleteTable =removes a table and all dependent objects from dynamodb

# data plane

- PutItem = put single item to table, specify preimary key attributes

- GetItem = get single item from table, specify primary key attributes

- Query = retrieves all items with specific partition key. must specify partition key value

- Scan = returns all items in specified table or index

- UpdateItem = modifies one or more attributes in an item

- DeleteItem = deletes single item, specify primary key

# naming rules

all names must be case-sensitive UTF8

table names and index names must be between 3 and 255 chars and regex [a-zA-Z0-9-_\.]

- attribute names must be at least one character

# data types

- scalar types: only one value (number, string, binary, boolean, null)

- document types: complex structure with nested attributes (list, map)

- set types: multiple scalar values (string set, number set, binary set)

DynamoDB is a NoSQL database and is schemaless.

you don't have to define any attributes or data types when you create tables

# local setup


