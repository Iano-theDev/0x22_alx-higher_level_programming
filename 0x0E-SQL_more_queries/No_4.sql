-- creates table unique_id on MySQL server
-- unique_id description: id is an int with default value of 1 & name is varchar(256)
-- database name will be passed as an argument of the mysql command
-- if the table unique_id already exists, the script should not fail

CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
