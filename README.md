# Logs Analysis Project

This project using data store in a PostgreSQL database will generate a report that respond to the following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

In  the script ```LogsAnalyser.py``` the report will be printed using the data extracted from the database with the functions in the ```dbModules.py``` module file.

## Installation

1. Clone this repo
2. Install Python 3.x (https://www.python.org/downloads)
3. Install pip tool for Python 3
4. Test you python intallation
    * Open a command line terminal
    * On that terminal run : ```python --version``` or ```python3 --version```
    * You should see a line with the python version you have installed
5. Install the Python PostgreSQL module using pip
    * Open a command line terminal
    * On that terminal run : ```pip3 install psycopg2```
6. Modify the connection string in the ```LogsAnalyser.py``` file to connect to your database
    * got to repo directory location on your machine
    * open the ```LogsAnalyser.py``` file in your favorite editor
    * on line #5 replace the value of the variable ```db_conn_string``` with your database connection data. 
    * For more info about the connection string you can visit : https://wiki.postgresql.org/wiki/Using_psycopg2_with_PostgreSQL
        


## Requerement

1. PostgreSQL database
2. A database with at least this elements
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

1. Open a command line terminal
2. On that terminal got to repo directory location on your machine
3. On that terminal run: ```python LogsAnalyser.py``` or ```python3 LogsAnalyser.py```