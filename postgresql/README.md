# postgresql

## setup (macOS native, built from source)

```
export postgres_install_dir=$HOME/pginstall
wget https://ftp.postgresql.org/pub/source/v12.14/postgresql-12.14.tar.gz -O p.tgz
tar xvzf p.tgz
cd postgresql-12.14/
./configure --prefix=$postgres_install_dir
nohup make -j20 && nohup make install
```

### starting postgres on mac

```
export postgres_dbdata=$HOME/pg-dbdata
cd $postgres_install_dir
cd bin
./pg_ctl -D $postgres_dbdata init
./pg_ctl -D $postgres_dbdata start
./createdb mydb
#./createuser --superuser myuser
./createuser --superuser myuser --pwprompt
psql postgres://127.0.0.1:5432/mydb -U myuser --password
```

## setup (ubuntu container)

```
$ apt install -y postgresql
$ export PG_VERSION=14 # PG_VERSION=12
$ pg_lsclusters
$ pg_ctlcluster $PG_VERSION main start
$ pg_ctlcluster $PG_VERSION main status
$ sudo su postgres
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
mydb=# grant all privileges on database mydb to myuser;
GRANT
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

```
psql -h my.database-url.com -p 5432 -d mydb -U myusername -W
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

## allow remote connections

postgres 14

```
pg_ctlcluster 14 main stop
echo "listen_addresses = '*'" >> /etc/postgresql/14/main/postgresql.conf
printf "host\tall\tall\t0.0.0.0/0\tscram-sha-256" >> /etc/postgresql/14/main/pg_hba.conf
printf "host\tall\tall\t::/0\tscram-sha-256" >> /etc/postgresql/14/main/pg_hba.conf
pg_ctlcluster 14 main start
```


postgres 12

```
pg_ctlcluster 12 main stop
echo "listen_addresses = '*'" >> /etc/postgresql/12/main/postgresql.conf
printf "host\tall\tall\t0.0.0.0/0\tmd5" >> /etc/postgresql/12/main/pg_hba.conf
printf "host\tall\tall\t::/0\tmd5" >> /etc/postgresql/12/main/pg_hba.conf
pg_ctlcluster 12 main start
```
ref : https://www.bigbinary.com/blog/configure-postgresql-to-allow-remote-connection

# JSONB array example

```
mydb=> create table mytable(data jsonb);
CREATE TABLE
mydb=> insert into mytable(data) values('["foo","bar","fee"]');
INSERT 0 1
mydb=> insert into mytable(data) values('["foo","fee"]');
INSERT 0 1
mydb=> select * from mytable;
         data          
-----------------------
 ["foo", "bar", "fee"]
 ["foo", "fee"]
(2 rows)

mydb=> select * from mytable where data ? 'fee';
         data          
-----------------------
 ["foo", "bar", "fee"]
 ["foo", "fee"]
(2 rows)

mydb=> select * from mytable where data ? 'bar';
         data          
-----------------------
 ["foo", "bar", "fee"]
(1 row)
```

# append/prepend strings

```
update mytable set mycolumn = 'foobar ' || mycolumn;
update mytable set mycolumn = mycolumn || ' fee';
```

# regex search

```
select name from mytable where name ~ '^test.+';
select name from mytable where name !~ '^blah.+';
```

# search with a list of values

```
select * from mytable where myvalue in ("a","b");
```

# JSON match

```
mydb=# create table abc(a jsonb);
CREATE TABLE
mydb=# insert into abc(a) values('["foo","bar"]');
INSERT 0 1
mydb=# select * from abc where a @> '["foo"]';
       a       
---------------
 ["foo", "bar"]
(1 row)

mydb=# insert into abc(a) values('["foo2","bar2"]');
INSERT 0 1
mydb=# select * from abc where a @> '["foo2"]';
        a        
-----------------
 ["foo2", "bar2"]
(1 row)
mydb=# insert into abc(a) values('{"fee":"fum"}');
INSERT 0 1
mydb=# select * from abc where a @> '{"fee":"fum"}';
       a        
----------------
 {"fee": "fum"}
(1 row)
```

# `GROUP BY` and `COUNT`

```
select field_name, count(field_name) from table_name where some_value @> '{"foo":"bar"}' group by field_name;
```

# print all tables in databasae

```
select table_name from information_schema.tables where table_schema = 'public'; 
```

# drop column from table

```
alter table mytable drop my_column;
```

# rename column

```
alter table mytable rename my_column to mycol;
```

# get type of column

```
select pg_typeof(my_column) from mytable;
```

# fix serial issues after db dump load

```
SELECT setval(pg_get_serial_sequence('mytable', 'id'), coalesce(max(id)+1, 1), false) FROM mytable;
```

# json query

if foobar_json is {"mydata":1} and type TEXT

```
select foobar_json::json ->> 'mydata' as mydata from my_requests where xid = '123123';
```
