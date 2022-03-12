DROP DATABASE	IF EXISTS test;
CREATE DATABASE test CHARSET='utf8';
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS class;
CREATE TABLE class(
	id int UNSIGNED PRIMARY KEY auto_increment NOT NULL,
	`name` varchar(20) DEFAULT ''
);
CREATE TABLE students ( 
	id INT UNSIGNED PRIMARY KEY auto_increment not null, 
	`name` VARCHAR ( 20 ) DEFAULT '',
	age TINYINT (100),
	height DECIMAL(5,2),
	gender enum('男','女'),
	cls_id INT UNSIGNED DEFAULT 0
);

alter table students add birthday DATE;
ALTER TABLE students change birthday birth DATE;
ALTER TABLE students MODIFY birth DATE not null;
ALTER TABLE students DROP birth;

insert into students values(0,'张三',20,170.1,1,1);
-- insert into students(`name`,age) values('李四',21);
insert into class values(0,'python1'),(0,'python2');
insert into students values( 0,'小明', 18, 180.00,2,1),
	( 0,'小月月', 18, 180.00, 2, 2 ),
	( 0,'彭于晏', 29, 185.00, 1, 1),
	( 0,'刘德华', 59, 175.00, 1, 2),
	( 0,'黄蓉', 38, 160.00, 2, 1 ),
	( 0,'凤姐', 28, 150.00, 2, 2),
	( 0,'王祖贤', 18, 172.00, 2, 1),
	( 0,'周杰伦', 36, NULL, 1, 1);

update students set `name`='熊大' where id=4;

DELETE from students where gender is NULL;

select s.id,s.name,s.gender from students as s;
select distinct gender from students;
select * from students where id>3;
select * from students where id<=3;
SELECT * from students where id!=3;
SELECT * from students where id<>3;

select * from students where id>3 and gender=2;
SELECT * from students where id>3 or name='张三';

select * from students where name like '小%';
select * from students where name like '小_';
select * from students WHERE name like '黄%' or name like '周%';


select * from students where id in(3,6);
select * from students where id BETWEEN 3 and 6;
select * from students where gender=1 and id between 3 and 6;


select * from students where gender=1 ORDER BY age;
select * from students where gender=1 ORDER BY age ASC;
select * from students where gender=1 ORDER BY age DESC;
select * from students ORDER BY age,height;

select * from students where height is null;
select * from students where height is not null;


select count(*) from students;
select count(*) from students where id>3;
select max(age) from students;
select min(height) from students;
select sum(age) from students where gender=1;
select avg(age) from students where gender=2;


-- select cls_id from students GROUP BY cls_id;
-- SELECT DISTINCT cls_id FROM students;
select max(age),cls_id,avg(height) from students GROUP BY cls_id;
select cls_id,GROUP_CONCAT(`name`) from students GROUP BY cls_id;
select cls_id,avg(age) FROM students GROUP BY cls_id HAVING avg(age)>27 ;
select gender,count(*) FROM students GROUP BY gender with ROLLUP;

select *,rank() over (partition by cls_id order by age desc) as rank1,
	dense_rank() over (partition by cls_id order by age desc) as dese_rank,
	row_number() over (partition by cls_id order by age desc) as row_num  from students;
									
									
select *,rank() over (order by age desc) as rank1,
	dense_rank() over (order by age desc) as dese_rank,
	row_number() over (order by age desc) as row_num  from students;
									
									
select * from students where gender=1 order by age desc limit 1,3;





-- mysqldump -u root -p python5 >python5.sql
-- create database test charset='utf8'
-- mysql -u root -p test<python5.sql
