CREATE TABLE class(
  id int auto_increment PRIMARY KEY,
  title CHAR(10) NOT NULL
)engine=innodb DEFAULT charset=UTF8;

-- 新增班级

insert into class(title) VALUE ("全栈4期");