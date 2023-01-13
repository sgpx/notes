# downloads

`https://dev.mysql.com/downloads/mysql/`

# setup (.tar.gz, fedora)

```
dnf install -y numa-devel libaio
useradd mysqluser
su mysqluser
cd ~
wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.31-linux-glibc2.17-aarch64.tar.gz -O m.tgz
tar xf m.tgz
mv -v mysql*/ mysql8/
mkdir dbdata
dbpath=$(realpath ~/dbdata)
./mysql8/mysqld --datadir $dbpath --initialize
./mysql8/mysqld --datadir $dbpath --bind-address 0.0.0.0 --port 5000
```

# get process list

```
show processlist;
```

# show databases

```
show databases;
```

# create database

```
create database testdb;
```

# create table

```
create table testdb.mytable(x int, y varchar(255) unique);
```

# insert values into table

```
insert into testdb.mytable(x,y) values(1, "a");
```

# select values 

```
use testdb;
select * from mytable;
```

# delete all entries in table

```
delete from mytable;
```

# drop table

```
use mydb;
drop table mytable;
```
