# MySQL on Ubuntu

## Installation
```
sudo apt-get install mysql-server
```

## Start and Stop the MySQL Server
```
sudo service mysql status

sudo service mysql stop

sudo service mysql start
```

## Connect as superuser root with the mysql client
```
sudo su
mysql -u root -p
```

## Create a Database and a Table
```
SHOW DATABASES;

CREATE DATABASE pets;

USE pets

CREATE TABLE cats
(
  id              INT unsigned NOT NULL AUTO_INCREMENT, # Unique ID for the record
  name            VARCHAR(150) NOT NULL,                # Name of the cat
  owner           VARCHAR(150) NOT NULL,                # Owner of the cat
  birth           DATE NOT NULL,                        # Birthday of the cat
  PRIMARY KEY     (id)                                  # Make the id the primary key
);

SHOW TABLES;

DESCRIBE cats;
```

## Add records into a table
```
INSERT INTO cats ( name, owner, birth) VALUES
  ( 'Sandy', 'Lennon', '2015-01-03' ),
  ( 'Cookie', 'Casey', '2013-11-13' ),
  ( 'Charlie', 'River', '2016-05-21' );
```

## Retrieve records from a table
```
SELECT * FROM cats;

SELECT name FROM cats WHERE owner = 'Casey';
```

## Delete a record from a table
```
DELETE FROM cats WHERE name='Cookie';
```

## Add or delete a column from a table
```
ALTER TABLE cats ADD gender CHAR(1) AFTER name;

DESCRIBE cats;
+--------+------------------+------+-----+---------+----------------+
| Field  | Type             | Null | Key | Default | Extra          |
+--------+------------------+------+-----+---------+----------------+
| id     | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name   | varchar(150)     | NO   |     | NULL    |                |
| gender | char(1)          | YES  |     | NULL    |                |
| owner  | varchar(150)     | NO   |     | NULL    |                |
| birth  | date             | NO   |     | NULL    |                |
+--------+------------------+------+-----+---------+----------------+
```

## More details on the table
```
SHOW CREATE TABLE cats\G
*************************** 1. row ***************************
       Table: cats
Create Table: CREATE TABLE `cats` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `gender` char(1) DEFAULT NULL,
  `owner` varchar(150) NOT NULL,
  `birth` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1
```

## Delete a column
```
ALTER TABLE cats DROP gender;

DESCRIBE cats;
+-------+------------------+------+-----+---------+----------------+
| Field | Type             | Null | Key | Default | Extra          |
+-------+------------------+------+-----+---------+----------------+
| id    | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name  | varchar(150)     | NO   |     | NULL    |                |
| owner | varchar(150)     | NO   |     | NULL    |                |
| birth | date             | NO   |     | NULL    |                |
+-------+------------------+------+-----+---------+----------------+
```