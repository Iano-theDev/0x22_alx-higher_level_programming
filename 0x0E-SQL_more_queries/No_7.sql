-- comments creates database my_school and table cities if the dont exist
-- describes table cities

CREATE DATABASE IF NOT EXISTS my_school;
CREATE TABLE IF NOT EXISTS my_school.cities (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) references my_school.states(id));
