create table tb1(x int, y int, z int);
create table tb2(v int, w int, x int);
insert into tb1(x,y,z) values(1,2,0),(1,3,6),(1,4,9),(2,12,23),(2,14,66);
insert into tb2(v,w,x) values(100,5,1),(200,6,2);
select * from tb1 left join tb2 on tb1.x = tb2.x;
select * from tb1 right join tb2 on tb1.x = tb2.x;
drop table tb1;
drop table tb2;