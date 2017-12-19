CREATE TABLE USER1 (
  id INT auto_increment PRIMARY KEY ,
  name CHAR(10) NOT NULL UNIQUE,
  age TINYINT NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;


-- 插入数据
INSERT INTO USER1(name, age) VALUES (%s, %s);
-- 删除数据
DELETE FROM USER1 WHERE id==%s;
-- 改
UPDATE USER1 SET age=%s WHERE name=%s;
-- 查
SELECT id,name,age from USER1;