CREATE DATABASE contact_info;

USE contact_info;

CREATE TABLE contacts (
  id INT PRIMARY KEY AUTO_INCREMENT,
  contact_name VARCHAR(100) NOT NULL,
  mobile_number VARCHAR(20) UNIQUE,
  email_id VARCHAR(100) UNIQUE
);
