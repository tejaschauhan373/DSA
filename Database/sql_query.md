# SQL Queries

### 1. Connect mysql in terminal
```
mysql -u user_name -p password dbname
```

### 2. Create Login
```
CREATE LOGIN MyLogin WITH PASSWORD = '123';
```

### 3. Create  User
* create user <user-name> for login <login-name>
```  
create user Guru99 for login MyLogin;
```

### 4. Create Database
* CREATE DATABASE databasename;
```  
CREATE DATABASE EDU_TSQL;
```

### 5. Granting Permission
* use <database-name>
* grant <permission-name> on <object-name> to <username\principle>
```
USE EDU_TSQL;
GO;
Grant select on Course to Guru99;
```

### 6. Create Table
```
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);
```

```
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
```

### 7. Insert into Table
* INSERT INTO <table_name> (column1, column2, column3 ) VALUES (value1, value2, value3);
```
INSERT INTO movie_entity (id, title, description, created, modified) VALUES (uuid_generate_v4(), 'Star Wars: Episode I - The Phantom Menace', 'The Phantom Menace is a 1999 American epic space-opera film written and directed by George Lucas, produced by Lucasfilm, distributed by 20th Century Fox and stars Liam Neeson, Ewan McGregor, Natalie Portman, Jake Lloyd, Ian McDiarmid, Anthony Daniels, Kenny Baker, Pernilla August, and Frank Oz', Now(), Now());
```

### 8. Select from table
* SELECT column1, column2 FROM table_name;
```
SELECT title, description FROM movie_entity;
```

### 9. Update into table
* UPDATE <table_name> SET column1 = value1, column2 = value2 WHERE <condition>;
```
UPDATE movie_entity SET title = 'Star Wars: Episode II - Attack of the Clones' WHERE title = 'Star Wars: Episode I - The Phantom Menace';
```

### 10. Delete from table
* DELETE FROM <table_name> WHERE <condition>;
```
DELETE FROM movie_entity WHERE title = 'Star Wars: Episode II - Attack of the Clones';
```

### 11. Delete table
* DROP TABLE <table_name>;
```
use TUTORIALS;
DROP TABLE tutorials_tbl;
```

### 12. Delete database
* DROP DATABASE <databasename>;
```
DROP DATABASE TUTORIALS;
```

### 13. Delete user
* DROP USER <username>@<hostname>;
```
DROP USER 'jeffrey'@'localhost';
```

### Advance query:
```
select id from students where batch = 2020 and id NOT IN (select id from failed_students);
```