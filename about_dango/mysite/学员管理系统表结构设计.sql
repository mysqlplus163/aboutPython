-- 创建班级表
CREATE TABLE class(
  id int auto_increment PRIMARY KEY,
  name CHAR(10) not null
)engine=innodb DEFAULT charset=utf8;


-- 创建学生表
CREATE TABLE student(
  id int auto_increment PRIMARY KEY,
  name CHAR(10) not null,
  class_id INT, FOREIGN KEY (class_id) REFERENCES class(id) ON DELETE CASCADE ON UPDATE CASCADE
)engine=innodb DEFAULT charset=utf8;

-- 创建老师表
CREATE TABLE teacher(
  id int auto_increment PRIMARY KEY,
  name CHAR(10) not null
)engine=innodb DEFAULT charset=utf8;

-- 创建老师和班级关系表
CREATE TABLE teacher2class(
  id INT AUTO_INCREMENT PRIMARY KEY,
  teacher_id INT,FOREIGN KEY (teacher_id) REFERENCES teacher(id) ON DELETE CASCADE ON UPDATE CASCADE ,
  class_id INT,FOREIGN KEY (class_id) REFERENCES class(id) ON DELETE CASCADE ON UPDATE CASCADE
)engine=innodb DEFAULT charset=utf8;