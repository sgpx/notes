# postgresql

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
