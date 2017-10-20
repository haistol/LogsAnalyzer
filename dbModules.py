import datetime
import psycopg2


def query_exec(db, query):
    """ Execute a query to the database passed as parameter """
    cmd = psycopg2.connect(db)
    cursor = cmd.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cmd.close()
    return result


def get_articles_views(db):
    """ Query the database to retrieve the articles and
    all the views they have """
    query = "SELECT a.title,count(l.path) AS views \
    FROM articles AS a \
    JOIN log AS l ON l.path LIKE concat('/article/', a.slug) \
    WHERE l.status LIKE '200 OK%' \
    GROUP by a.id ORDER by views DESC;"
    return query_exec(db, query)


def get_authors_views(db):
    """ Query the database to retrieve the authors and
    the sum of the views all their articles """
    query = "SELECT au.name,count(l.path) AS views \
    FROM articles AS a \
    JOIN authors AS au ON a.author = au.id \
    JOIN log AS l ON l.path LIKE concat('/article/', a.slug) \
    WHERE l.status like '200 OK%' \
    GROUP by name ORDER by views DESC"
    return query_exec(db, query)


def get_error_count(db):
    """ Query the database to get the error percent of each day """
    query = "SELECT to_char(date_trunc('day',l.time),'yyyy-mm-dd') as day, \
    p.error*100.0 /count(*)  as error_percent \
    from log as l \
    join (select to_char(date_trunc('day',time),'yyyy-mm-dd') as day ,\
    count(status) as error \
    from log \
    where status <>'200 OK' \
    group by to_char(date_trunc('day',time),'yyyy-mm-dd')) as p \
    on to_char(date_trunc('day',l.time),'yyyy-mm-dd') = p.day \
    group by to_char(date_trunc('day',l.time),'yyyy-mm-dd'),p.error \
    order by error_percent DESC"
    return query_exec(db, query)
