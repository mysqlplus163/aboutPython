CREATE DATABASE IF NOT EXISTS TEST1 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;

CREATE TABLE IF NOT EXISTS `table1`(
   `runoob_id` INT UNSIGNED AUTO_INCREMENT,
   `runoob_title` VARCHAR(100) NOT NULL,
   `runoob_author` VARCHAR(40) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `runoob_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `table1`(
  `user_id` INT UNSIGNED AUTO_INCREMENT,
  `user_name` CHAR NOT NULL,
  `sex` TINYINT NOT NULL ,
  PRIMARY KEY (`user_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO table1(`user_id`, `user_name`, `sex`) VALUES (1, "张三", 1);

ALTER TABLE table1 MODIFY `user_name` VARCHAR(12);


SELECT `user_id`, `user_name`, `sex` FROM table1;


CREATE TABLE userinfo (
  uid BIGINT AUTO_INCREMENT PRIMARY KEY ,
  name CHAR(20),
  department_id INT,
  CONSTRAINT fk_userinfo_d1 FOREIGN KEY (`department_id`) REFERENCES d1 (`id`)
)