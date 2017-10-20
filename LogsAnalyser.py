import dbModules
import datetime


db_conn_string = "dbname=news"


def error_day_percentage(data):
    """ Print all the days that have more than 1% of fail
    requests """
    for row in data:
        if float(row[1]) > 1.0:
            print("*", datetime.datetime.strptime(
                row[0], '%Y-%m-%d').strftime('%B %d, %Y'),
                "- {:.2f}% errors".format(float(row[1])))


def popular_three_articles(data):
    """ Print the three articles with more views """
    for row in range(len(data)):
        if row == 3:
            return
        print("*", data[row][0], "-", data[row][1], "views")


def popular_authors(data):
    """ Print all the authors and their views"""
    for row in (data):
        print("*", row[0], "-", row[1], "views")


print("What are the most popular three articles of all time?")
print()
data = dbModules.get_articles_views(db_conn_string)
popular_three_articles(data)
print()
print("Who are the most popular article authors of all time?")
print()
data = dbModules.get_authors_views(db_conn_string)
popular_authors(data)
print()
print("On which days did more than 1% of requests lead to errors?")
print()
data = dbModules.get_error_count(db_conn_string)
error_day_percentage(data)
