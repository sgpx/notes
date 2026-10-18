create table mytable(data jsonb);
insert into mytable(data) values('["foo","bar","baz"]');
insert into mytable(data) values('["foo","baz"]');
select * from mytable;
select * from mytable where data ? 'baz';
select * from mytable where data ? 'bar';
