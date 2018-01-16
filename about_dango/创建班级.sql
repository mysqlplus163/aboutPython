-- 创建班级表
CREATE TABLE class(
  id int auto_increment PRIMARY KEY,
  title CHAR(10) NOT NULL
)engine=innodb DEFAULT charset=UTF8;

-- 新增班级

insert into class(title) VALUE ("全栈X期");

CREATE TABLE user(
  id int auto_increment PRIMARY KEY,
  name CHAR(10) NOT NULL,
  habit CHAR(20) NOT NULL
)engine=innodb DEFAULT charset=UTF8;
