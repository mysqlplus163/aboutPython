-- 创建班级表
CREATE TABLE class(
  id int auto_increment PRIMARY KEY,
  name CHAR(10) not null
)engine=innodb DEFAULT charset=utf8;


-- 创建学生表
CREATE TABLE student(
  id int auto_increment PRIMARY KEY,
  name CHAR(10) not null,
  class_id INT REFERENCES class(id)
)engine=innodb DEFAULT charset=utf8;

-- 创建老师表
CREATE TABLE teacher(
  id int auto_increment PRIMARY KEY,
  name CHAR(10) not null
)engine=innodb DEFAULT charset=utf8;

-- 创建老师和班级关系表
CREATE TABLE teacher2class(
  id INT AUTO_INCREMENT PRIMARY KEY,
  teacher_id int REFERENCES teacher(id),
  class_id int REFERENCES class(id)
)engine=innodb DEFAULT charset=utf8;