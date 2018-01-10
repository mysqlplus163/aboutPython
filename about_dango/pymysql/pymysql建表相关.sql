CREATE TABLE userinfo(
id INT AUTO_INCREMENT PRIMARY KEY,
username CHAR (10) NOT NULL,
password CHAR (20) NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;


-- 插入数据
INSERT INTO userinfo(username, password) VALUES("alex", "alexdsb");

-- 检索
SELECT id FROM userinfo WHERE username=%s and password=$s