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
