-- Script that creates the database hbtn_0d_usa and the table cities.
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES state(id),
	name VARCHAR(256) NOT NULL
);
