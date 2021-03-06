# postgresql

## setup (ubuntu container)

```
$ apt install -y postgresql
$ pg_ctlcluster 12 main start
$ pg_ctlcluster 12 main status
$ su postgres
$ psql
```

## examples

creating a table and a user

```
$ psql
psql (12.9 (Ubuntu 12.9-0ubuntu0.20.04.1))
Type "help" for help.

postgres=# create database mydb;
CREATE DATABASE
postgres=# \c mydb;
You are now connected to database "mydb" as user "postgres".
mydb=# create table mytable(a int, b text);
CREATE TABLE
mydb=# insert into mytable(a,b) values(1,'hello world');
INSERT 0 1
mydb=# select * from mytable;
 a |      b      
---+-------------
 1 | hello world
(1 row)

mydb=# create user myuser with password 'mypassword';
CREATE ROLE
mydb=# grant all privileges on mydb to myuser;
ERROR:  relation "mydb" does not exist
mydb=# grant all privileges on mytable to myuser;
GRANT
mydb=# \dt+
                     List of relations
 Schema |  Name   | Type  |  Owner   | Size  | Description 
--------+---------+-------+----------+-------+-------------
 public | mytable | table | postgres | 16 kB | 
(1 row)

mydb=# \q
```

logging in with created user

```
psql --username="myuser" --password --host="127.0.0.1" --port="5432" --dbname="mydb"
Password: 
psql (12.9 (Ubuntu 12.9-0ubuntu0.20.04.1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.

mydb=>
```

connect with postgres URI

```
# psql "postgresql://myuser:mypassword@127.0.0.1:5432/mydb"
psql (12.9 (Ubuntu 12.9-0ubuntu0.20.04.1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.

mydb=> 
```

## installing psql client on macOS (homebrew)

```
$ brew install libpq
$ alias psql=/opt/homebrew/opt/libpq/bin/psql
$ echo 'alias psql=/opt/homebrew/opt/libpq/bin/psql' > ~/.zshrc
$ psql --version
psql (PostgreSQL) 14.1
```

## syntax

sql statements are semicolon terminated

## connecting to database with URI connection string

`postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]`

## select database

`\\c mydb`

## list tables and relations

`\\dt+`

## create table

`create table tablename(a type_a, b type_b, ....);`

example: `create table mytable( a int, b int)`

## insert into table

`insert into mytable(a,b) values(1,2);`


## example

```
$ psql postgres://myuser:mypwd@abc.com:5432/mydb

mydb-> \dt
Did not find any relations.
mydb-> \dt+
Did not find any relations.
mydb-> \? 
mydb=> create table abc(x int , y int );
CREATE TABLE
mydb=> \dt+
                                      List of relations
 Schema | Name | Type  |     Owner      | Persistence | Access method |  Size   | Description 
--------+------+-------+----------------+-------------+---------------+---------+-------------
 public | abc  | table |     myuser     | permanent   | heap          | 0 bytes | 
(1 row)

mydb=> insert into abc(x,y) values(1,2);
INSERT 0 1
mydb=> select * from abc;
 x | y 
---+---
 1 | 2
(1 row)

mydb=> \q
$
```

## force SSL

```
$ psql postgres://myuser:mypwd@abc.com:5432/mydb?sslmode=require
```


```
$ psql postgres://myuser:mypwd@abc.com:5432/mydb?requiressl=true
```
