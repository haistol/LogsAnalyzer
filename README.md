# Logs Analysis Project

This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

In  the script `LogsAnalyser.py` the report will be printed using the data extracted from the database with the functions in the `dbModules.py` module file.

## Installation

1. Clone this repo.
2. Install Python 3.x (https://www.python.org/downloads).
3. Install pip tool for Python 3.
4. Test your Python installation.
    * Open a command line terminal.
    * On that terminal run : `python --version` or `python3 --version`.
    * You should see a line with the python version you have installed.
5. Install the Python PostgreSQL module using pip.
    * Open a command line terminal.
    * On that terminal run : `pip3 install psycopg2`.
6. Install PostgreSQL database (https://www.postgresql.org/download)
7. Configure the PostgreSQL (https://www.postgresql.org/docs/10/static/tutorial-start.html).
8. Extract the database dump
    * Go to repo directory location on your machine.
    * Unzip the content of the file `newsdata.zip` in the same directory
9. Open a command line terminal.
10. Enter to the postgres command line interface.
    * On that terminal run: `psql` or `psql -U <username>`.
11. Create a database named "news"
    * On the psql command line interface enter the command: `CREATE DATABASE news;`
    * Verify that the database has been created enter the command: `\l`  to see the list off elements.
12. Exit the psql command line interface unsing `\q` command.
13. Create the tables and populate with data.
    * On that terminal go to repo directory location on your machine.
    * On that terminal run: `psql news < newsdata.sql` or if you have diferend user for the protgreSQL `psql -U <username> news < newsdata.sql`.
14. Verify the database content.
    * On that terminal run: `psql news` or `psql -U <username> news`.
    * On the psql command line interface enter the command `\d` to see the list of tables in the database.
15. The database structure is:
    * Table name: authors 
        - Columns:
            name (text),
            bio (text),
            id (integer)
    * Table name: articles
        - Columns:
            author (integer),
            title (text),
            slug (text),
            lead (text),
            body (text),
            time (timestamp),
            id (integer) 
    * Table name: log
        - Columns:
            path (text),
            ip (inet),
            method (text),
            status (text),
            time (timestamp),
            id (integer)


## Run Step

1. Open a command line terminal.
2. On that terminal go to repo directory location on your machine.
3. On that terminal run: `python LogsAnalyser.py` or `python3 LogsAnalyser.py`.