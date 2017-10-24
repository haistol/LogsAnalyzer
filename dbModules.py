import datetime
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


DBNAME = 'news'


def query_exec(query):
    """ Execute a query to the database passed as parameter """
    try:
        cmd = psycopg2.connect(dbname=DBNAME)
        cursor = cmd.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cmd.close()
        return result
    except psycopg2.Error as e:
        if e.pgcode is not None:
            print(e.pgcode, "-", e.pgerror)
            return []
        else:
            print("Error Connecting to database:", DBNAME)
            exit()
    except:
        print("Unknown Error has occurred")
        exit()


def get_articles_views():
    """ Query the database to retrieve the articles and
    all the views they have """
    query = """SELECT a.title, count(l.path) AS views
    FROM articles AS a
    JOIN log AS l
    ON l.path = concat('/article/', a.slug)
    WHERE l.status LIKE '200 OK%'
    GROUP by a.id
    ORDER by views DESC
    LIMIT 3;"""
    return query_exec(query)


def get_authors_views():
    """ Query the database to retrieve the authors and
    the sum of the views all their articles """
    query = """SELECT au.name, count(l.path) AS views
    FROM articles AS a
    JOIN authors AS au
    ON a.author = au.id
    JOIN log AS l
    ON l.path = concat('/article/', a.slug)
    WHERE l.status like '200 OK%'
    GROUP by name
    ORDER by views DESC;"""
    return query_exec(query)


def get_error_count():
    """ Query the database to get the error percent of each day """
    query = """SELECT l.day,
    (p.error*100.0 /l.total) as error_percent
    from (SELECT time::date as day,
    count(*) as total
    FROM log
    group by time::date) as l
    join (select time::date as day,
    count(status) as error
    from log
    where status <>'200 OK'
    group by time::date) as p
    on l.day = p.day
    WHERE  (p.error*100.0 /l.total)>1.0
    order by error_percent DESC;"""
    return query_exec(query)
