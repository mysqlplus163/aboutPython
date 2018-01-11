-- 创建学生表
CREATE TABLE student(
  id int auto_increment PRIMARY KEY,
  name CHAR(10) not null,
  class_id int not null,
  CONSTRAINT fk_student_class FOREIGN KEY(class_id) REFERENCES class(id)
)engine=innodb DEFAULT charset=utf8;

SELECT * FROM student left JOIN class on student.class_id = class.id


ALTER TABLE student ALTER COLUMN name CHAR(10) not null;

-- 插入学生数据
INSERT INTO student(name, class_id) VALUES ("张三",5);

-- 查询学生表
SELECT * from student LEFT JOIN class on student.class_id = class.id;

select student.id, student.name, class.title from student left join class on student.class_id = class.id;