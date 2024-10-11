# SQL - Introduction

### Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    What’s a database
    What’s a relational database
    What does SQL stand for
    What’s MySQL
    How to create a database in MySQL
    What does DDL and DML stand for
    How to CREATE or ALTER a table
    How to SELECT data from a table
    How to INSERT, UPDATE or DELETE data
    What are subqueries
    How to use MySQL functions


### Requirements

    Allowed editors: vi, vim, emacs
    All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
    All your files should end with a new line
    All your SQL queries should have a comment just before (i.e. syntax above)
    All your files should start by a comment describing the task
    All SQL keywords should be in uppercase (SELECT, WHERE…)
    A README.md file, at the root of the folder of the project, is mandatory
    The length of your files will be tested using wc

## Tasks

0. List databases

    Write a script that lists all databases of your MySQL server.


1. Create a database

    Write a script that creates the database hbtn_0c_0 in your MySQL server.

        If the database hbtn_0c_0 already exists, your script should not fail
        You are not allowed to use the SELECT or SHOW statements


2. Delete a database

    Write a script that deletes the database hbtn_0c_0 in your MySQL server.

        If the database hbtn_0c_0 doesn’t exist, your script should not fail
        You are not allowed to use the SELECT or SHOW statements


3. List tables

    Write a script that lists all the tables of a database in your MySQL server.

        The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)


4. First table

    Write a script that creates a table called first_table in the current database in your MySQL server.

        first_table description:
            id INT
            name VARCHAR(256)
        The database name will be passed as an argument of the mysql command
        If the table first_table already exists, your script should not fail
        You are not allowed to use the SELECT or SHOW statements


5. Full description

    Write a script that prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server.

    The database name will be passed as an argument of the mysql command
    You are not allowed to use the DESCRIBE or EXPLAIN statements


6. List all in table

    Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

        All fields should be printed
        The database name will be passed as an argument of the mysql command


7. First add

    Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

        New row:
            id = 89
            name = Best School
        The database name will be passed as an argument of the mysql command


8. Count 89

    Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

    The database name will be passed as an argument of the mysql command


9. Full creation

    Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

    second_table description:
        id INT
        name VARCHAR(256)
        score INT
    The database name will be passed as an argument to the mysql command
    If the table second_table already exists, your script should not fail
    You are not allowed to use the SELECT and SHOW statements
    Your script should create these records:
        id = 1, name = “John”, score = 10
        id = 2, name = “Alex”, score = 3
        id = 3, name = “Bob”, score = 14
        id = 4, name = “George”, score = 8


10. List by best

    Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

    Results should display both the score and the name (in this order)
    Records should be ordered by score (top first)
    The database name will be passed as an argument of the mysql command


11. Select the best

    Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

        Results should display both the score and the name (in this order)
        Records should be ordered by score (top first)
        The database name will be passed as an argument of the mysql command


12. Cheating is bad

    Write a script that updates the score of Bob to 10 in the table second_table.

        You are not allowed to use Bob’s id value, only the name field
        The database name will be passed as an argument of the mysql command


13. Score too low

    Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

        The database name will be passed as an argument of the mysql command


14. Average

    Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

        The result column name should be average
        The database name will be passed as an argument of the mysql command


15. Number by score

    Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

        The result should display:
            the score
            the number of records for this score with the label number
        The list should be sorted by the number of records (descending)
        The database name will be passed as an argument to the mysql command


16. Say my name

    Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

        Don’t list rows without a name value
        Results should display the score and the name (in this order)
        Records should be listed by descending score
        The database name will be passed as an argument to the mysql command
    In this example, new data have been added to the table second_table.
